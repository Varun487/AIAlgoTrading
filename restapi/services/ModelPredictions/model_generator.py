# REQUIRED IMPORTS
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import datetime

import warnings
warnings.filterwarnings("ignore")

import ta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(98)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.models import load_model

from sklearn import metrics
from sklearn.preprocessing import StandardScaler

# CONFIGURATIONS OF MODELS TO GENERATE
prediction_periods = [2, 3, 5, 7, 10]
train_test_split_factors = [0.8, 0.8, 0.75, 0.75, 0.8]
activation = 'relu'
optimizer = 'adam'
loss = 'mse'
epochs = [20, 50, 20, 50, 30]
hidden_layer_configs = [(8, 32, 8), (100, 200, 100), (12, 32, 32, 12), (25, 75, 100, 75, 25), (100, 64, 64)]


# AUTOMATE MODEL GENERATION
class ModelGenerator(object):
    def __init__(self):
        self.models_count = 0

    def run(self):
        companies_data = os.listdir('./services/ModelPredictions/Storage/CompanyData/')

        # For each company, generate models according to differrent configurations
        for company_csv in companies_data:
            print()
            print("===================================================================")
            print()

            print(f"Generating models for {company_csv}")

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

                prediction_period = prediction_periods[i]

                # Split into test and train sets
                msk = np.random.rand(len(company_df)) < train_test_split_factors[i]
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

                # Define model
                model = Sequential()
                model.add(
                    LSTM(hidden_layer_configs[i][0], activation=activation, return_sequences=True, input_shape=(89, 1)))
                for layer in range(1, len(hidden_layer_configs[i]) - 1):
                    model.add(LSTM(hidden_layer_configs[i][layer], activation=activation, return_sequences=True))
                model.add(LSTM(hidden_layer_configs[i][-1], activation=activation))
                model.add(Dense(1))
                model.compile(optimizer=optimizer, loss=loss)

                # Show a summary of the model
                print()
                model.summary()

                # String to save model
                save_string = f'./services/ModelPredictions/Storage/Models/{company_csv[:-7]}/' \
                              f'LSTM_period:{prediction_period}_splitfactor:{train_test_split_factors[i]}_' \
                              f'epochs:{epochs[i]}.h5'

                # Train model
                checkpoint = ModelCheckpoint(save_string, monitor='loss', verbose=1, save_best_only=True, mode='auto',
                                             period=1)
                model.fit(X_train_standard_scaled, y_train_standard_scaled, epochs=epochs[i], batch_size=1,
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
                              f'LSTM_period:{prediction_period}_splitfactor:{train_test_split_factors[i]}_' \
                              f'epochs:{epochs[i]}_nmae:{normalized_mae}_nmse:{normalized_mse}' \
                              f'_nrmse:{normalized_rmse}_mae:{actual_mae}_mse:{actual_mse}_rmse:{actual_rmse}_.h5'
                os.rename(save_string, new_save_string)

                # Consider building just one model for now
                break

            # Consider just one company for now
            break
