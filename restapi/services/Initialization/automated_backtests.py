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
        self.step = step
        self.msg = msg

    def run(self):
        if self.data is None:
            raise ValueError("No data given!")

        # Conduct backtests for each company
        for company in self.companies:

            company_strategy_configs = list(StrategyConfig.objects.filter(
                                                strategy_type__name='Simple Bollinger Band Strategy'
                                       )) + \
                                       list(StrategyConfig.objects.filter(
                                                strategy_type__name='LSTM Strategy',
                                                lstm_company=company,
                                       ))

            # Conduct backtests with all possible strategy configurations for that company
            for i in range(len(company_strategy_configs)):
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
                    print(f"    Running Backtest: {self.backtest_count}/2000"
                          f" - {company} {company_strategy_configs[i]}")

                    # Run backtest
                    BackTestReportGenerator(
                        df=self.df,
                        ticker_time_period=self.data['ticker_time_periods'][i],
                        indicator_time_period=company_strategy_configs[i].indicator_time_period,
                        dimension=company_strategy_configs[i].get_dimension_display(),
                        sigma=company_strategy_configs[i].sigma,
                        factor=company_strategy_configs[i].take_profit_factor,
                        max_holding_period=company_strategy_configs[i].max_holding_period,
                        company=company,
                        strategy_type=company_strategy_configs[i].strategy_type,
                        indicator=self.data['indicators'][i],
                        strategy_config=company_strategy_configs[i],
                        signal_generator=self.data['signal_generators'][i],
                        take_profit_stop_loss=self.data['take_profit_and_stop_losses'][i],
                        order_executor=self.data['order_executors'][i],
                        trade_evaluator=self.data['trade_evaluators'][i],
                    ).generate_backtest_report()

        print(f"STEP {self.step}: {self.msg}")
