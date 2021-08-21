import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import warnings

warnings.filterwarnings("ignore")

from ta import add_all_ta_features

from .signalgenerator import SignalGenerator
from strategies.models import StrategyConfig

from services.ModelPredictions.predictions import Predictions
from ..SourceData.sourcedata import SourceData


class LSTMSignalGenerator(SignalGenerator):
    def __init__(self, indicator=None, strategy_config=None):
        super().__init__(indicator)
        self.strategy_config = strategy_config
        self.valid_strategy_config = False

    def validate_strategy_config(self):
        self.valid_strategy_config = isinstance(self.strategy_config, StrategyConfig)

    def generate_signals(self):
        # Compute indicators on input df
        self.set_indicator_df()
        self.signal_df = self.indicator_df.copy()

        # Get predictions
        self.signal_df = Predictions(
            df=self.signal_df,
            ticker=self.strategy_config.lstm_company.ticker,
            period=self.strategy_config.lstm_model_time_period
        ).get_prediction()

        # Generate signals
        signals = []

        for predicted_percent in self.signal_df['prediction']:
            if predicted_percent > self.strategy_config.lstm_buy_threshold:
                signals.append('BUY')
            elif predicted_percent < self.strategy_config.lstm_sell_threshold:
                signals.append('SELL')
            else:
                signals.append('FLAT')

        self.signal_df['SIGNAL'] = signals

        # Return signals
        return self.signal_df
