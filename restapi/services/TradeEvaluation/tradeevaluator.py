from services.Utils.converter import Converter


class TradeEvaluator(object):
    def __init__(self, df=None, dimension=None):
        self.df = df
        self.dimension = dimension

        self.valid_df = False
        self.valid_dimension = False
        self.valid = False

        self.calc_df = df

    def validate_df(self):
        self.valid_df = Converter(df=self.df).validate_df() and all(col in self.df.columns for col in
                                                                    ['order_entry_price', 'order_exit_price',
                                                                     'order_entry_index', 'order_exit_index'])

    def validate_dimension(self):
        self.valid_dimension = self.dimension in ['open', 'high', 'low', 'close']

    def validate(self):
        self.validate_df()
        self.validate_dimension()
        self.valid = self.valid_df and self.valid_dimension

    def evaluate_trade(self):
        # Evaluates each trade
        print("Evaluate trade method called")

    def evaluate_all_trades(self):
        # Evaluates all trades in df
        # Calls evaluate_trade method for each trade encountered
        print("Evaluate all trades method called")
        self.evaluate_trade()
        return self.calc_df

    def get_evaluated_df(self):
        self.validate()
        if self.valid:
            return self.evaluate_all_trades()
        else:
            raise ValueError("Either the df or dimension or both are invalid!")
