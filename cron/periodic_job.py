import sys

try:
    # Adding a path for easier imports
    sys.path.append('/home/app/microservice/AITradingPlatform/')

    from datetime import datetime, timedelta
    from django.utils.timezone import make_aware

    # Opening log file
    log = open("/home/app/microservice/cron/cronlog", "a+")
    print(f'{datetime.now()}: CRON JOB EXECUTED', file=log)

    from django import setup
    from django.conf import settings

    from AITradingPlatform import AITradingPlatform_cron_settings_defaults

    # Configuring settings to run a stand alone django application
    settings.configure(AITradingPlatform_cron_settings_defaults)

    # To initialize the new app
    setup()

    print(file=log)
    print(' DJANGO STAND ALONE APP SETUP SUCCESSFUL!', file=log)

    # Get required models
    from DataFeeder.models import Company, ImmutableData
    from DataFeeder.utils import get_data_on_demand
    from PaperTrader.models import PaperTradedStrategies, PaperTradeOrder
    from Strategies.models import Orders
    from Strategies.utils import simple_bollinger_bands_strategy

    # REAL TIME SOURCING FOR ALL COMPANIES

    print(file=log)
    print(" ----- ----- ----- ----- -----", file=log)
    print(file=log)

    print(" DATAFEEDER - REAL TIME SOURCING", file=log)
    print(file=log)

    # for all companies in db which use Yahoo finance to source data
    for company_obj in Company.objects.filter(data_provider='Yahoo'):

        all_sourced_data = ImmutableData.objects.order_by('time_stamp').filter(company=company_obj)

        if len(all_sourced_data) > 0:
            latest_dt = all_sourced_data[len(all_sourced_data) - 1].time_stamp
            latest_dt -= timedelta(days=10)

            now_dt = make_aware(datetime.now())
            now_dt = now_dt.replace(hour=0, minute=0, second=0, microsecond=0)

            collected_data, data_not_found = get_data_on_demand([company_obj.ticker], 'Yahoo', latest_dt, now_dt,
                                                                'daily', 'year1month1')

            new_sourced_data = ImmutableData.objects.order_by('time_stamp').filter(company=company_obj)

            print(f" Collected data for {company_obj.ticker} from {latest_dt} to {now_dt} and pushed to DB.", file=log)
        else:
            print(f" No data for {company_obj.ticker} in DB. No data sourced.", file=log)

    print(file=log)
    print(" ----- ----- ----- ----- -----", file=log)
    print(file=log)

    # PAPER TRADER

    # TRACK / UPDATE LIVE ORDERS

    print(" PAPERTRADER - TRACK ORDERS REAL TIME", file=log)
    print(file=log)

    print(file=log)
    print(" ----- ----- ----- ----- -----", file=log)
    print(file=log)


    # GENERATE NEW ORDERS BASED ON LATEST DATA

    print(" PAPERTRADER - GENERATE ORDERS REAL TIME", file=log)
    print(file=log)

    for strategy in PaperTradedStrategies.objects.all():
        # print(strategy)
        # print(strategy.strategy)

        if strategy.strategy.name == 'Simple Bollinger Bands Strategy':
            slice = 'year1month1'

            now_dt = make_aware(datetime.now())
            now_dt = now_dt.replace(hour=0, minute=0, second=0, microsecond=0)

            start_dt = now_dt - timedelta(strategy.time_period + 1)

            collected_data, data_not_found, df = simple_bollinger_bands_strategy(strategy.company.ticker, 'Yahoo', start_dt,
                                                                                 now_dt, 'daily', slice,
                                                                                 strategy.column, strategy.time_period,
                                                                                 strategy.sigma)

            if df.empty:
                print(f" NO new orders generated for {strategy.company} on {now_dt}, using Paper Traded Strategy {strategy.name}", file=log)
            else:
                ord_type = 'G'

                if df['Orders'][0] == 'BUY':
                    ord_type = 'B'
                if df['Orders'][0] == 'SHORT':
                    ord_type = 'S'

                company_obj = Company.objects.get(ticker=strategy.company.ticker)

                if not Orders.objects.filter(order_type=ord_type, order_category='M', company=company_obj, time_stamp=now_dt):
                    Orders(
                        order_type=ord_type,
                        order_category='M',
                        company=company_obj,
                        time_stamp=now_dt
                    ).save()

                order = Orders.objects.get(order_type=ord_type, order_category='M', company=company_obj, time_stamp=now_dt, profit_loss=0.0, quantity=0)

                if not PaperTradeOrder.objects.filter(order=order):
                    PaperTradeOrder(
                        order=order,
                        strategy=strategy,
                        live_order=True,
                    ).save()

                print(f" NEW Order generated for {strategy.company} on {now_dt}, using Paper Traded Strategy {strategy.name}", file=log)

    print(file=log)
    print(" ----- ----- ----- ----- -----", file=log)
    print(file=log)

    # remove added path
    sys.path.pop()

    print(" EXECUTION SUCCESS!", file=log)

except Exception as e:
    print(' ' + str(e), file=log)

    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno

    print(" Exception type: ", exception_type, file=log)
    print(" File name: ", filename, file=log)
    print(" Line number: ", line_number, file=log)

print(file=log)
print("----- x ----- x ----- x ----- x -----", file=log)
print(file=log)
