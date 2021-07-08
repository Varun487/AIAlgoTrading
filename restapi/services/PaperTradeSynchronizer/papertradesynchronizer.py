import datetime

from services.PaperTradeEvaluator.papertradeevaluator import PaperTradeEvaluator
from services.CompanyQuotes.companyquotes import CompanyQuotes
from services.PaperSignalExecutor.papersignalexecutor import PaperSignalExecutor
from services.PaperSignalGeneration.papersignalgenerator import PaperSignalGenerator


class PaperTradeSynchronizer(object):
    def __init__(self, test_end_date=None, test_today=None):
        self.test_end_date = test_end_date
        self.test_today = test_today
        self.log_file = open("/home/app/restapi/services/PaperTradeSynchronizer/log.txt", "a+")

    def run(self):

        print(file=self.log_file)
        print("--------- RUN PAPER TRADE SYNCHRONIZER ----------", file=self.log_file)
        print(f"Date Time: {datetime.datetime.now()}", file=self.log_file)

        CompanyQuotes().update()

        print(f"Updated Company Quotes to latest data", file=self.log_file)

        PaperTradeEvaluator().run()

        print(f"Evaluated current paper trades", file=self.log_file)

        PaperSignalExecutor().run()

        print(f"Executed paper signals", file=self.log_file)

        PaperSignalGenerator(test_end_date=self.test_end_date, test_today=self.test_today).run()

        print(f"Generated Paper signals", file=self.log_file)
