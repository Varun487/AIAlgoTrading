from papertrader.models import CurrentQuote
from papertrader.models import PaperSignal
from papertrader.models import PaperTrade

from strategies.models import Order
from strategies.models import Trade


class PaperSignalExecutor(object):
    def __init__(self):
        self.paper_signal = None
        self.company = None
        self.current_company_quote = None
        self.paper_traded_strategy = None
        self.signal = None

    def execute_signal(self):
        # Create and push entry order
        entry_order = Order(
            signal=self.signal,
            ticker_data=self.current_company_quote.ticker_data
        )
        entry_order.save()

        # Create and push trade
        trade = Trade(
            entry_order=entry_order,
            duration=0,
            net_return=0,
            return_percent=0,
        )
        trade.save()

        # Create and push paper trade
        PaperTrade(
            paper_traded_strategy=self.paper_traded_strategy,
            live=True,
            trade=trade,
        ).save()

        # Mark paper signal as executed
        self.paper_signal.executed = True
        self.paper_signal.save()

    def run(self):
        # Get all live paper signals
        live_paper_signals = list(PaperSignal.objects.filter(executed=False))

        for paper_signal in live_paper_signals:
            # Set paper signal
            self.paper_signal = paper_signal

            # Set signal
            self.signal = paper_signal.signal

            # Set paper traded strategy
            self.paper_traded_strategy = paper_signal.paper_traded_strategy

            # Set company
            self.company = paper_signal.paper_traded_strategy.company

            # Set current company quote
            self.current_company_quote = CurrentQuote.objects.filter(company=self.company)[0]

            # Execute paper signal
            self.execute_signal()
