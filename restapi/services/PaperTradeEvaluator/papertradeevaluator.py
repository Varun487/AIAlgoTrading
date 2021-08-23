from papertrader.models import CurrentQuote
from papertrader.models import PaperTrade

from strategies.models import Order
from strategies.models import TickerData


class PaperTradeEvaluator(object):
    def __init__(self):
        self.paper_trade = None
        self.company = None
        self.company_current_quote = None
        self.strategy_config = None
        self.trade = None
        self.take_profit = None
        self.stop_loss = None

    def update_paper_trade(self):
        # Update net return
        self.trade.net_return = self.company_current_quote.ticker_data.close - self.paper_trade.trade.entry_order.ticker_data.close
        if self.trade.entry_order.signal.type == "2":
            self.trade.net_return *= -1

        # Update return %
        self.trade.return_percent = (self.trade.net_return / self.paper_trade.trade.entry_order.ticker_data.close) * 100
        if self.trade.entry_order.signal.type == "2":
            self.trade.return_percent *= -1

        # Update duration
        self.trade.duration += 1

        self.trade.save()

    def set_take_profit_and_stop_loss(self):
        self.take_profit = self.paper_trade.take_profit
        self.stop_loss = self.paper_trade.stop_loss

    def exit_trade(self):
        close_price = self.company_current_quote.ticker_data.close

        reached_max_holding = self.trade.duration >= self.strategy_config.max_holding_period
        signal_trigger = close_price > self.take_profit or close_price < self.stop_loss

        if self.trade.entry_order.signal.type == "2":
            signal_trigger = close_price < self.take_profit or close_price > self.stop_loss

        # If conditions to exit trade are met
        if reached_max_holding or signal_trigger:

            # Create a ticker data obj
            updated_ticker = TickerData(
                time_stamp=self.company_current_quote.ticker_data.time_stamp,
                open=self.company_current_quote.ticker_data.open,
                high=self.company_current_quote.ticker_data.high,
                low=self.company_current_quote.ticker_data.low,
                close=self.company_current_quote.ticker_data.close,
                volume=self.company_current_quote.ticker_data.volume,
                company=self.company,
                time_period="1"
            )
            updated_ticker.save()

            # Create an exit order
            exit_order = Order(
                signal=self.paper_trade.trade.entry_order.signal,
                ticker_data=updated_ticker
            )
            exit_order.save()

            # Update trade
            self.trade.exit_order = exit_order
            self.trade.save()

            # Mark paper trade as historical
            self.paper_trade.live = False
            self.paper_trade.save()

    def run(self):
        # Get all live paper trades
        live_paper_trades = list(PaperTrade.objects.filter(live=True))

        total = len(live_paper_trades)
        count = 0

        for paper_trade in live_paper_trades:

            # Set paper trade
            self.paper_trade = paper_trade

            # Set company
            self.company = paper_trade.paper_traded_strategy.company

            # Set current quote of company
            self.company_current_quote = CurrentQuote.objects.filter(company=self.company)[0]

            # Set strategy config
            self.strategy_config = paper_trade.paper_traded_strategy.strategy_config

            # Set trade
            self.trade = paper_trade.trade

            # Update paper trade
            self.update_paper_trade()

            # Get take profit and stop loss
            self.set_take_profit_and_stop_loss()

            # Exit trade (if required)
            self.exit_trade()

            count += 1
            print(f"Paper Trade evaluated for {count}/{total} - {paper_trade}")
