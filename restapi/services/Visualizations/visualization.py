from backtester.models import BackTestReport


class Visualization(object):
    def __init__(self, backtest_report=None, height=-1, width=-1):

        self.backtest_report = backtest_report
        self.height = height
        self.width = width

        self.valid_backtest_report = False
        self.valid_height = False
        self.valid_width = False
        self.valid = False

    def validate_height(self):
        self.valid_height = (type(self.height) == int) and (self.height > 0)

    def validate_width(self):
        self.valid_width = (type(self.width) == int) and (self.width > 0)

    def validate_backtest_report(self):
        self.valid_backtest_report = isinstance(self.backtest_report, BackTestReport)

    def validate(self):
        self.validate_height()
        self.validate_width()
        self.validate_backtest_report()
        self.valid = self.valid_height and self.valid_width and self.valid_backtest_report

    def generate_visualization(self):
        pass

    def get_visualization(self):
        self.validate()
        if self.valid:
            return self.generate_visualization()
        else:
            raise ValueError("The inputs given are invalid!")
