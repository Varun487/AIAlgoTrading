from ta import add_all_ta_features

from .signalgenerator import SignalGenerator
from strategies.models import StrategyConfig

from ..SourceData.sourcedata import SourceData


class LSTMSignalGenerator(SignalGenerator):
    def __init__(self, indicator=None, strategy_config=None):
        super().__init__(indicator)
        self.strategy_config = strategy_config
        self.valid_strategy_config = False

    def validate_strategy_config(self):
        self.valid_strategy_config = isinstance(self.strategy_config, StrategyConfig)

    def generate_signals(self):
        self.set_indicator_df()
        self.signal_df = self.indicator_df.copy()

        self.signal_df = add_all_ta_features(self.signal_df, open="open", high="high", low="low", close="close",
                                             volume="volume", fillna=True)

        # print(self.signal_df)
        # print(self.signal_df.columns)

        return self.signal_df
