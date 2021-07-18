from strategies.models import Company
from strategies.models import StrategyConfig
from strategies.models import TickerData

from services.Utils.getters import Getter
from services.BackTestReportGeneration.backtestreportgenerator import BackTestReportGenerator


class AutomatedBacktests(object):
    def __init__(self, step=0, msg="", data=None):
        self.data = data
        self.backtest_count = 0
        self.df = None
        self.companies = list(Company.objects.all())
        self.strategy_configs = list(StrategyConfig.objects.all())
        self.step = step
        self.msg = msg

    def run(self):
        if self.data is None:
            raise ValueError("No data given!")

        # Conduct backtests for each company
        for company in self.companies:

            # Conduct each company conduct a backtest with all possible strategy configurations
            for i in range(len(self.strategy_configs)):

                # Getter returns a dataframe if data is present
                # Getter returns an empty list if no data is present
                self.df = Getter(TickerData, True, {
                    "company": company,
                    "time_stamp__range": self.data['date_ranges'][i],
                }).get_data()

                # If data exists in db
                if type(self.df) != list:

                    # Modify dataframe
                    self.df.drop(['id', 'company_id', 'time_period'], axis=1, inplace=True)
                    self.df.set_index('time_stamp', inplace=True)
                    self.df.reset_index(inplace=True)

                    # Increment backtest count
                    self.backtest_count += 1

                    # Output Current Status
                    print(f"    Running Backtest: {self.backtest_count}/{len(self.companies)*len(self.strategy_configs)}"
                          f" - {company} {self.strategy_configs[i]}")

                    # Run backtest
                    BackTestReportGenerator(
                        df=self.df,
                        ticker_time_period=self.data['ticker_time_periods'][i],
                        indicator_time_period=self.strategy_configs[i].indicator_time_period,
                        dimension=self.strategy_configs[i].get_dimension_display(),
                        sigma=self.strategy_configs[i].sigma,
                        factor=self.strategy_configs[i].take_profit_factor,
                        max_holding_period=self.strategy_configs[i].max_holding_period,
                        company=company,
                        strategy_type=self.strategy_configs[i].strategy_type,
                        indicator=self.data['indicators'][i],
                        strategy_config=self.strategy_configs[i],
                        signal_generator=self.data['signal_generators'][i],
                        take_profit_stop_loss=self.data['take_profit_and_stop_losses'][i],
                        order_executor=self.data['order_executors'][i],
                        trade_evaluator=self.data['trade_evaluators'][i],
                    ).generate_backtest_report()

        print(f"STEP {self.step}: {self.msg}")
