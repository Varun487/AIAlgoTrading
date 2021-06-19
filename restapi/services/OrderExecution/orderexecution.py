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
        entry_indexes = []
        for i in range(len(self.calc_df)):
            if (i != (len(self.calc_df) - 1)) and (self.calc_df["SIGNAL"][i] != "FLAT"):
                entry_prices.append(self.calc_df[self.dimension][i + 1])
                entry_indexes.append(i + 1)
            else:
                entry_prices.append(-1)
                entry_indexes.append(-1)
        self.calc_df["order_entry_price"] = entry_prices
        self.calc_df["order_entry_index"] = entry_indexes

    # def get_exit_orders(self):
    #     """Order exits when exit signal is generated"""
    #     exit_prices = []
    #     exit_indexes = []
    #
    #     # iterate through all orders
    #     for i in range(len(self.calc_df)):
    #
    #         # if an entry order is present
    #         if self.calc_df['order_entry_index'][i] != -1:
    #
    #             # if max_holding period is within the backtesting data
    #             if (i + self.max_holding_period) < (len(self.calc_df) - 1):
    #
    #                 order_exited = False
    #                 calc_df_slice = self.calc_df.iloc[i + 1:i + self.max_holding_period + 1]
    #                 stop_loss = self.calc_df['stoploss'][i]
    #                 take_profit = self.calc_df['takeprofit'][i]
    #                 signal = self.calc_df['SIGNAL'][i]
    #
    #                 print()
    #                 print(calc_df_slice)
    #                 print(stop_loss, take_profit, signal)
    #
    #                 for j in range(len(calc_df_slice)):
    #                     order_exited = False
    #                     price = calc_df_slice[self.dimension][i+j+1]
    #                     print(price)
    #
    #                     if signal == 'BUY' and (price > take_profit or price < stop_loss):
    #                         order_exited = True
    #                         exit_prices.append(price)
    #                         exit_indexes.append(i+j+1)
    #                         break
    #
    #                     if signal == "SELL" and (price > stop_loss or price < )
    #
    #                 if not order_exited:
    #                     exit_prices.append(price)
    #                     exit_indexes.append(i + j + 1)
    #
    #         # No entry order present
    #         else:
    #             exit_indexes.append(-1)
    #             exit_prices.append(-1)

    def execute(self):
        self.validate()
        if self.valid:
            self.calc_df = self.df.copy()
            self.get_entry_orders()
            # self.get_exit_orders()
            # print()
            # print(self.calc_df)
            return self.calc_df
        else:
            raise ValueError("Either df, max_holding_period or dimension is not valid!")
