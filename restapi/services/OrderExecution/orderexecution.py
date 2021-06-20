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
                        and ("take_profit" in self.df.columns) and ("stop_loss" in self.df.columns)

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

        # iterate through all signals
        for i in range(len(self.calc_df)):
            # If signal is not flat and there is enough data to last through the max holding period + 1 of the order
            if ((i + self.max_holding_period + 1) <= (len(self.calc_df) - 1)) and (self.calc_df["SIGNAL"][i] != "FLAT") and i != 0:
                entry_prices.append(self.calc_df[self.dimension][i + 1])
                entry_indexes.append(i + 1)
            else:
                entry_prices.append(-1)
                entry_indexes.append(-1)
        self.calc_df["order_entry_price"] = entry_prices
        self.calc_df["order_entry_index"] = entry_indexes

    def get_exit_orders(self):
        """Order exits the day after exit signal is generated"""
        exit_prices = []
        exit_indexes = []

        # iterate through all orders
        for i in range(len(self.calc_df)):
            # if an entry order is present, determine the exit order price and index
            if self.calc_df['order_entry_index'][i] != -1:
                # get order info and df with data from max holding period
                calc_df_slice = self.calc_df.iloc[i + 1:i + self.max_holding_period + 2]
                stop_loss = self.calc_df['stop_loss'][i]
                take_profit = self.calc_df['take_profit'][i]
                signal = self.calc_df['SIGNAL'][i]
                order_executed = False

                # iterate through all prices in holding period and see if order closes
                for j in range(len(calc_df_slice) - 1):
                    current_price = calc_df_slice[self.dimension][j + i + 1]
                    exit_price = calc_df_slice[self.dimension][j + i + 2]
                    exit_index = j + i + 2

                    if signal == "BUY" and ((current_price > take_profit) or (current_price < stop_loss)) and (not order_executed):
                        exit_prices.append(exit_price)
                        exit_indexes.append(exit_index)
                        order_executed = True

                    elif signal == "SELL" and ((current_price < take_profit) or (current_price > stop_loss)) and (not order_executed):
                        exit_prices.append(exit_price)
                        exit_indexes.append(exit_index)
                        order_executed = True

                # if the order doesn't close, close it at max holding period
                if not order_executed:
                    last_index = calc_df_slice.index[-1]
                    exit_prices.append(calc_df_slice[self.dimension][last_index])
                    exit_indexes.append(last_index)

            # No entry order present
            else:
                exit_indexes.append(-1)
                exit_prices.append(-1)

        self.calc_df['order_exit_price'] = exit_prices
        self.calc_df['order_exit_index'] = exit_indexes

    def execute(self):
        self.validate()
        if self.valid:
            self.calc_df = self.df.copy()
            self.get_entry_orders()
            self.get_exit_orders()
            # print()
            # print(self.calc_df)
            # self.calc_df.to_csv('/home/app/restapi/services/OrderExecution/execution.csv', index=False)
            return self.calc_df
        else:
            raise ValueError("Either df, max_holding_period or dimension is not valid!")
