from services.Utils.converter import Converter


class TradeEvaluator(object):
    def __init__(self, df=None):
        self.df = df
        self.valid_df = False
        self.valid = False
        self.calc_df = df

    def validate_df(self):
        self.valid_df = Converter(df=self.df).validate_df() and all(col in self.df.columns for col in
                                                                    ['order_entry_price', 'order_exit_price',
                                                                     'order_entry_index', 'order_exit_index'])

    def validate(self):
        self.validate_df()
        self.valid = self.valid_df

    def evaluate_trade(self, index):
        # Evaluates each trade
        signal = self.calc_df['SIGNAL'][index]
        entry_price = self.calc_df['order_entry_price'][index]
        exit_price = self.calc_df['order_exit_price'][index]
        entry_index = self.calc_df['order_entry_index'][index]
        exit_index = self.calc_df['order_exit_index'][index]

        net_return = exit_price - entry_price

        if signal == "SELL":
            net_return *= -1

        return_percentage = (net_return / entry_price) * 100
        duration = exit_index - entry_index

        return net_return, return_percentage, duration

    def evaluate_all_trades(self):
        # Evaluates all trades in df
        trade_net_returns = []
        trade_return_percentages = []
        trade_durations = []

        for i in range(len(self.calc_df)):
            if self.calc_df['order_entry_index'][i] != -1:
                trade_net_return, trade_return_percentage, trade_duration = self.evaluate_trade(i)

                trade_net_returns.append(trade_net_return)
                trade_return_percentages.append(trade_return_percentage)
                trade_durations.append(trade_duration)

            else:
                trade_net_returns.append(None)
                trade_return_percentages.append(None)
                trade_durations.append(None)

        self.calc_df['trade_net_return'] = trade_net_returns
        self.calc_df['trade_return_percentage'] = trade_return_percentages
        self.calc_df['trade_duration'] = trade_durations

        return self.calc_df

    def get_evaluated_df(self):
        self.validate()
        if self.valid:
            return self.evaluate_all_trades()
        else:
            raise ValueError("Either the df or dimension or both are invalid!")
