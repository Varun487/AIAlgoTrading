from services.Utils.converter import Converter


class CalcTakeProfitStopLoss(object):
    def __init__(self, df=None, factor=-1):
        self.df = df
        self.calc_df = None
        self.factor = factor
        self.valid = False
        self.valid_df = False
        self.valid_factor = False

    def validate_df(self):
        self.valid_df = Converter(df=self.df).validate_df() and ("SIGNAL" in self.df.columns)

    def validate_factor(self):
        self.valid_factor = (type(self.factor) == int) and (self.factor > 0)

    def validate(self):
        self.validate_df()
        self.validate_factor()
        self.valid = self.valid_df and self.valid_factor

    def generate_prices(self):
        self.calc_df = self.df

    def get_calc_df(self):
        self.validate()
        self.generate_prices()
        if self.valid:
            return self.calc_df
        else:
            raise ValueError("Either data frame or factor are not valid!")


class TakeProfitAndStopLossBB(CalcTakeProfitStopLoss):
    def __init__(self, df=None, factor=-1, dimension=None):
        super().__init__(df, factor)
        self.dimension = dimension
        self.valid_dimension = False

    def validate_dimension(self):
        self.valid_dimension = self.dimension in ["open", "low", "high", "close"]

    def validate(self):
        super().validate()
        self.validate_dimension()
        self.valid = self.valid and self.valid_dimension

    def generate_prices(self):
        """Take profit and stop loss generated on the basis of signal price"""

        temp_df = self.df.copy()
        take_profit = [-1]
        stop_loss = [-1]

        for i in range(1, len(temp_df)):
            if temp_df["SIGNAL"][i] != "FLAT" and i != 0:

                # Absolute difference of the prev close price and current close price * factor
                risk = abs(temp_df[self.dimension][i] - temp_df[self.dimension][i - 1]) * self.factor
                dimension_plus_risk = temp_df[self.dimension][i] + risk
                dimension_minus_risk = temp_df[self.dimension][i] - risk

                if temp_df['SIGNAL'][i] == 'BUY':
                    take_profit.append(dimension_plus_risk)
                    stop_loss.append(dimension_minus_risk)
                else:
                    take_profit.append(dimension_minus_risk)
                    stop_loss.append(dimension_plus_risk)

            else:
                take_profit.append(-1)
                stop_loss.append(-1)

        temp_df["take_profit"] = take_profit
        temp_df["stop_loss"] = stop_loss

        # print()
        # print(temp_df)

        self.calc_df = temp_df
