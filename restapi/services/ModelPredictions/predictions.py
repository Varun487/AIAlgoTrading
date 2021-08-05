import os
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

class Predictions(object):
    def __init__(self, df=None, ticker=None, period=None, split_factor=None, epochs=None):
        self.ticker = ticker
        self.period = period
        self.split_factor = split_factor
        self.epochs = epochs
        self.df = df
        self.df_pred = None
        self.valid = False

        self.all_companies_path = './services/ModelPredictions/Storage/Models/'

    def validate(self):
        valid_period = type(self.period) == int and self.period > 0
        valid_split_factor = type(self.split_factor) == float and 0 < self.split_factor < 1
        valid_epochs = type(self.epochs) == int and self.epochs > 0
        valid_ticker = type(self.ticker) == str and self.ticker[:-3] in os.listdir(self.all_companies_path)
        valid_df = (self.df is not None) and (type(self.df) == pd.DataFrame) and (not self.df.empty)

        if valid_ticker and valid_epochs and valid_period and valid_split_factor and valid_df:
            self.valid = True

    def generate_prediction(self):
        pred_model = f'LSTM_period:{self.period}_splitfactor:{self.split_factor}_epochs:{self.epochs}'
        company = f'{self.all_companies_path}{self.ticker[:-3]}/'
        model = None

        for model_path in os.listdir(company):
            if model_path[:len(pred_model)] == pred_model:
                model = load_model(company+model_path)

        if model is None:
            raise ValueError("Model of given configuration does not exist!")

        # Set scaler
        scaler = StandardScaler()

        self.df_pred = self.df.copy()

        self.df_pred.drop(['time_stamp'], axis=1, inplace=True)

        self.df_pred = self.df_pred.values

        self.df_pred = scaler.fit_transform(self.df_pred)

        self.df_pred = self.df_pred.reshape(self.df_pred.shape[0], self.df_pred.shape[1], 1)

        predictions = model.predict(self.df_pred)

        predicted_percent_return = scaler.inverse_transform(predictions)

        print(predictions.shape)

        return "abc"

    def get_prediction(self):
        self.validate()
        if self.valid:
            return self.generate_prediction()
        else:
            raise ValueError("Invalid inputs!")
