import datetime

from django.utils.timezone import make_aware

from papertrader.models import CurrentQuote
from strategies.models import Company, TickerData

from services.SourceData.sourcedata import SourceData


class CompanyQuotes(object):
    def __init__(self, companies=None):
        self.companies = companies
        self.valid = False

        # Set up dates
        self.start_date = make_aware(datetime.datetime.now() - datetime.timedelta(days=7))
        self.end_date = make_aware(datetime.datetime.now())

        self.df = None
        self.df_last_row = None

    def validate_each_company_in_companies(self):
        all_companies_are_valid = True
        for company in self.companies:
            all_companies_are_valid = all_companies_are_valid and isinstance(company, Company)
        return all_companies_are_valid

    def validate(self):
        if self.companies is None:
            self.companies = list(Company.objects.all())
            self.valid = True
        else:
            self.valid = (type(self.companies) == list) and (self.companies != []) and \
                         self.validate_each_company_in_companies()

    def create_or_update_current_quote(self):
        count = 0
        total = len(self.companies)

        for company in self.companies:

            # Source data for company
            self.df = SourceData(company=company, start_date=self.start_date, end_date=self.end_date).get_df()
            self.df.reset_index(inplace=True)
            self.df_last_row = self.df.iloc[len(self.df) - 1]

            # Create a new ticker data object and push to DB
            updated_ticker = TickerData(
                time_stamp=make_aware(self.df_last_row['Date']),
                open=self.df_last_row['Open'],
                high=self.df_last_row['High'],
                low=self.df_last_row['Low'],
                close=self.df_last_row['Close'],
                volume=self.df_last_row['Volume'],
                company=company,
                time_period="1"
            )
            updated_ticker.save()

            # Create/Update current quote
            quote = CurrentQuote.objects.filter(company=company)
            if not quote:
                # Create current quote
                cq = CurrentQuote(
                    company=company,
                    ticker_data=updated_ticker,
                    last_updated=make_aware(datetime.datetime.now()),
                )
                cq.save()

            else:
                # Update current quote
                quote.update(ticker_data=updated_ticker, last_updated=make_aware(datetime.datetime.now()))

            count += 1
            print(f"Updating quote for {count}/{total} - {company}")

    def update(self):
        self.validate()
        if self.valid:
            self.create_or_update_current_quote()
        else:
            raise ValueError("The companies list given is incorrect!")
