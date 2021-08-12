import os
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler


class Predictions(object):
    def __init__(self, df=None, ticker=None, period=None):
        self.ticker = ticker
        self.period = period
        self.df = df
        self.model = None
        self.df_pred = None
        self.valid = False

        self.all_companies_path = './services/ModelPredictions/Storage/Models/'

    def validate(self):
        valid_period = type(self.period) == int and self.period in [2, 3, 5, 7, 9]
        valid_ticker = type(self.ticker) == str and self.ticker[:-3] in os.listdir(self.all_companies_path)
        valid_df = (self.df is not None) and (type(self.df) == pd.DataFrame) and (not self.df.empty)

        if valid_ticker and valid_period and valid_df:
            self.valid = True

    def generate_prediction(self):

        # Load model
        for m in os.listdir(f'{self.all_companies_path}{self.ticker[:-3]}/'):
            if int(m[12:13]) == self.period:
                self.model = load_model(f'{self.all_companies_path}{self.ticker[:-3]}/{m}')

        # Print summary
        # self.model.summary()

        # Scale data
        scaler = StandardScaler()
        self.df_pred = self.df.copy()
        # print(self.df_pred.shape)
        self.df_pred.drop(['time_stamp'], axis=1, inplace=True)
        self.df_pred = self.df_pred.values
        self.df_pred = scaler.fit_transform(self.df_pred)
        self.df_pred = self.df_pred.reshape(self.df_pred.shape[0], self.df_pred.shape[1], 1)

        # Get predictions
        predictions = self.model.predict(self.df_pred)
        scaler.fit(predictions)
        predicted_percent_return = scaler.inverse_transform(predictions)
        self.df['prediction'] = predicted_percent_return

        return self.df

    def get_prediction(self):
        self.validate()
        if self.valid:
            return self.generate_prediction()
        else:
            raise ValueError("Invalid inputs!")
