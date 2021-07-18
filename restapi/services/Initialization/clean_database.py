# Get all required models
from django.contrib.auth.models import User

from strategies.models import ExampleStrategiesModel
from strategies.models import Company
from strategies.models import TickerData
from strategies.models import IndicatorType
from strategies.models import StrategyType
from strategies.models import StrategyConfig
from strategies.models import Signal
from strategies.models import Order
from strategies.models import Trade
from strategies.models import VisualizationType

from backtester.models import ExampleBackTesterModel
from backtester.models import BackTestReport
from backtester.models import BackTestTrade

from papertrader.models import ExamplePaperTraderModel
from papertrader.models import PaperTradedStrategy
from papertrader.models import CurrentQuote
from papertrader.models import PaperTrade
from papertrader.models import PaperSignal


class CleanDatabase(object):
    def __init__(self):
        self.db_tables = [User, PaperSignal, PaperTrade, CurrentQuote, PaperTradedStrategy, ExamplePaperTraderModel,
                          BackTestTrade, BackTestReport, ExampleBackTesterModel,
                          VisualizationType, Trade, Order, Signal, StrategyConfig, StrategyType, IndicatorType,
                          TickerData, Company, ExampleStrategiesModel]

    def run(self):
        for table in self.db_tables:
            table.objects.all().delete()
        print("STEP 1: All data deleted from DB")
