from services.Utils.converter import Converter


class OrderExecution(object):
    def __init__(self, df=None, max_holding_period=-1, dimension=None):
        self.df = df
        self.max_holding_period = max_holding_period
        self.dimension = dimension

        self.calc_df = None

        self.valid_df = False
        self.valid_max_holding_period = False
        self.valid_dimension = False
        self.valid = False

    def validate_df(self):
        self.valid_df = Converter(df=self.df).validate_df() and ("SIGNAL" in self.df.columns) \
                        and ("takeprofit" in self.df.columns) and ("stoploss" in self.df.columns)

    def validate_max_holding_period(self):
        self.valid_max_holding_period = (type(self.max_holding_period) == int) and (self.max_holding_period > 0)

    def validate_dimension(self):
        self.valid_dimension = self.dimension in ["open", "high", "low", "close"]

    def validate(self):
        self.validate_df()
        self.validate_max_holding_period()
        self.validate_dimension()
        self.valid = self.valid_df and self.valid_max_holding_period and self.valid_dimension

    def get_entry_orders(self):
        entry_prices = []
        for i in range(len(self.calc_df)):
            if (i != (len(self.calc_df) - 1)) and (self.calc_df["SIGNAL"][i] != "FLAT"):
                entry_prices.append(self.calc_df[self.dimension][i + 1])
            else:
                entry_prices.append(-1)
        return entry_prices

    def get_exit_order_prices():
        exit_prices = []
        for i in range(len(self.calc_df)):
            if (i != (len(self.calc_df) - 1)) and (self.calc_df["SIGNAL"][i] != "FLAT"):
                entry_prices.append(self.calc_df[self.dimension][i + 1])
            else:
                entry_prices.append(-1)
        return entry_prices

    def execute(self):
        self.validate()
        if self.valid:
            self.calc_df = self.df.copy()
            self.get_entry_orders()
            self.calc_df["entry_order_price"] = self.get_entry_order_prices()
            # self.calc_df["exit_order_price"] = self.get_exit_order_prices()
            # print("valid!")
            print()
            print(self.calc_df)
            return self.calc_df
        else:
            raise ValueError("Either df, max_holding_period or dimension is not valid!")
