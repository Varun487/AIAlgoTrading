valid_indicator_list = ["Indicator", "BollingerIndicator"]


class SignalGenerator(object):
    def __init__(self, indicator=None):
        self.indicator = indicator
        self.valid_indicator = False
        self.indicator_df = None
        self.signal_df = None

    def validate_indicator(self):
        self.valid_indicator = (self.indicator is not None) and (type(self.indicator).__name__ in valid_indicator_list)

    def set_indicator_df(self):
        self.validate_indicator()
        if self.valid_indicator:
            self.indicator_df = self.indicator.calc()
        else:
            raise TypeError("Indicator given is not valid!")

    def generate_signals(self):
        # All inherited classes must return the signal df
        self.set_indicator_df()
        return self.indicator_df

    def get_signals(self):
        self.signal_df = self.generate_signals()
        return self.signal_df
