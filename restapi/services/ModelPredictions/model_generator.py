# REQUIRED IMPORTS
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings

warnings.filterwarnings("ignore")

import ta
import pandas as pd
import numpy as np

np.random.seed(98)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint

from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# CONFIGURATIONS OF MODELS TO GENERATE
prediction_periods = [2, 3, 5, 7, 9]
train_test_split_factor = 0.8
activation = 'relu'
optimizer = 'adam'
loss = 'mse'
epochs = 35
hidden_layer_configs = [10, 15, 20, 25, 30]


# AUTOMATE MODEL GENERATION
class ModelGenerator(object):
    def __init__(self):
        self.models_count = 0

    def run(self):
        companies_data = os.listdir('./services/ModelPredictions/Storage/CompanyData/')

        company_count = 0

        # For each company, generate models according to differrent configurations
        for company_csv in companies_data:
            print()
            print(f"Generating models for Company {company_count+1} / 50 -> {company_csv}")
            print()

            company_df = pd.read_csv(f'./services/ModelPredictions/Storage/CompanyData/{company_csv}')

            # Calculate returns according to prediction periods in config
            for prediction_period in prediction_periods:
                company_df[f'returns_period_{prediction_period}'] = list(company_df['close'][prediction_period:]) + [
                    None for i in range(prediction_period)]
                company_df[f'returns_period_{prediction_period}'] = ((company_df[
                                                                          f'returns_period_{prediction_period}'] -
                                                                      company_df['close']) / company_df['close']) * 100
            company_df.dropna(inplace=True)

            # Create 5 models per company
            for i in range(5):

                # Don't re-run model if it already exists
                try:
                    continue_flag = False
                    for f in os.listdir(f'./services/ModelPredictions/Storage/Models/{company_csv[:-7]}/'):
                        if f[:48] == f"LSTM_period:{prediction_periods[i]}_model:{hidden_layer_configs[i]}_splitfactor:0.8_epochs:35":
                            continue_flag = True
                    if continue_flag:
                        continue
                except:
                    pass

                print()
                print("===================================================================")
                print()

                prediction_period = prediction_periods[i]

                # Split into test and train sets
                msk = np.random.rand(len(company_df)) < train_test_split_factor
                train_df = company_df.copy()[msk]
                test_df = company_df.copy()[~msk]

                # Train set
                X_train = train_df.copy()
                X_train.drop(list(X_train.filter(regex='returns')) + ['time_stamp'], axis=1, inplace=True)
                y_train = train_df.copy()[f'returns_period_{prediction_period}']

                # Test set
                X_test = test_df.copy()
                X_test.drop(list(X_test.filter(regex='returns')) + ['time_stamp'], axis=1, inplace=True)
                y_test = test_df.copy()[f'returns_period_{prediction_period}']

                # Add indicators
                X_train = ta.add_all_ta_features(X_train, open="open", high="high", low="low", close="close",
                                                 volume="volume", fillna=True)
                X_test = ta.add_all_ta_features(X_test, open="open", high="high", low="low", close="close",
                                                volume="volume", fillna=True)

                # Scale and Reshape datasets

                # Set scaler
                scaler = StandardScaler()

                # Scale and Reshape X_train
                X_train_standard_scaled = X_train.values
                X_train_standard_scaled = scaler.fit_transform(X_train_standard_scaled)
                X_train_standard_scaled = X_train_standard_scaled.reshape(X_train_standard_scaled.shape[0],
                                                                          X_train_standard_scaled.shape[1], 1)

                # Scale and Reshape X_test
                X_test_standard_scaled = X_test.values
                X_test_standard_scaled = scaler.fit_transform(X_test_standard_scaled)
                X_test_standard_scaled = X_test_standard_scaled.reshape(X_test_standard_scaled.shape[0],
                                                                        X_test_standard_scaled.shape[1], 1)

                # Scale and Reshape y_train
                y_train_standard_scaled = y_train.values
                y_train_standard_scaled = y_train_standard_scaled.reshape(y_train_standard_scaled.shape[0], 1)
                y_train_standard_scaled = scaler.fit_transform(y_train_standard_scaled)

                # Scale and Reshape y_test
                y_test_standard_scaled = y_test.values
                y_test_standard_scaled = y_test_standard_scaled.reshape(y_test_standard_scaled.shape[0], 1)
                y_test_standard_scaled = scaler.fit_transform(y_test_standard_scaled)

                print()
                print(f"MODEL {(company_count * 5) + i + 1} / 250 -> {company_csv}")
                print()

                # Define model
                model = Sequential()
                model.add(LSTM(hidden_layer_configs[i], activation=activation, input_shape=(89, 1)))
                model.add(Dense(1))
                model.compile(optimizer=optimizer, loss=loss)

                # Show a summary of the model
                model.summary()
                print()

                # String to save model
                save_string = f'./services/ModelPredictions/Storage/Models/{company_csv[:-7]}/' \
                              f'LSTM_period:{prediction_period}_splitfactor:{train_test_split_factor}_' \
                              f'epochs:{epochs}.h5'

                try:
                    # Train model
                    checkpoint = ModelCheckpoint(save_string, monitor='loss', verbose=1, save_best_only=True, mode='auto',
                                             period=1)
                    model.fit(X_train_standard_scaled, y_train_standard_scaled, epochs=epochs, batch_size=1,
                          callbacks=[checkpoint])

                    # Test model
                    predictions = model.predict(X_test_standard_scaled)
                    prediction_percents = scaler.inverse_transform(predictions)

                    # For normalized return
                    normalized_mae = metrics.mean_absolute_error(y_test_standard_scaled, predictions)
                    normalized_mse = metrics.mean_squared_error(y_test_standard_scaled, predictions)
                    normalized_rmse = np.sqrt(metrics.mean_squared_error(y_test_standard_scaled, predictions))

                    print()
                    print('ERROR VALUES FOR NORMALIZED RETURN PERCENTS')
                    print('Mean Absolute Error:', normalized_mae)
                    print('Mean Squared Error:', normalized_mse)
                    print('Root Mean Squared Error:', normalized_rmse)

                    # For actual return percents
                    actual_mae = metrics.mean_absolute_error(y_test, prediction_percents)
                    actual_mse = metrics.mean_squared_error(y_test, prediction_percents)
                    actual_rmse = np.sqrt(metrics.mean_squared_error(y_test, prediction_percents))

                    print()
                    print('ERROR VALUES FOR ACTUAL RETURN PERCENTS')
                    print('Mean Absolute Error:', actual_mae)
                    print('Mean Squared Error:', actual_mse)
                    print('Root Mean Squared Error:', actual_rmse)

                    # Rename saved model with more info
                    new_save_string = f'./services/ModelPredictions/Storage/Models/{company_csv[:-7]}/' \
                                      f'LSTM_period:{prediction_period}_model:{hidden_layer_configs[i]}_' \
                                      f'splitfactor:{train_test_split_factor}_' \
                                      f'epochs:{epochs}_nmae:{normalized_mae}_nmse:{normalized_mse}' \
                                      f'_nrmse:{normalized_rmse}_mae:{actual_mae}_mse:{actual_mse}_rmse:{actual_rmse}_.h5'
                    os.rename(save_string, new_save_string)

                    print()
                    print(f"Model saved to: {new_save_string}")
                    print()

                except:
                    continue

                # Consider building just one model for now
                # break

            # Consider just one company for now
            # break

            company_count += 1
