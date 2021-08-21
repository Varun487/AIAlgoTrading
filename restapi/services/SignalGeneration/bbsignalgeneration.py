from .signalgenerator import SignalGenerator


class BBSignalGenerator(SignalGenerator):
    """Generates signals for BB strategy, returns empty df if no signals produced"""
    def __init__(self, indicator=None, strategy_config=None):
        super().__init__(indicator)

    def generate_signals(self):
        self.set_indicator_df()
        signals_df = self.indicator_df.copy()
        signals = []
        for i in range(len(self.indicator_df)):
            if self.indicator_df['bb_bbhi'][i] != 0.0:
                signals.append("SELL")
            elif self.indicator_df['bb_bbli'][i] != 0.0:
                signals.append("BUY")
            else:
                signals.append("FLAT")

        signals_df["SIGNAL"] = signals
        signals_df.set_index(self.indicator.dimension, inplace=True)
        signals_df.reset_index(inplace=True)

        return signals_df
