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

    # Get all paper trader live orders
    lpt_order_obj = PaperTradeOrder.objects.filter(live_order=True)

    # print(lpt_order_obj)

    # Decide when to close orders

    for lpt_order in lpt_order_obj:
        if lpt_order.order.order_type == "G":
            # get_out_strategy = lpt_order.strategy
            # print(get_out_strategy)
            # print(PaperTradeOrder.objects.filter(live_order=True, strategy=lpt_order.strategy))

            for pt_order_dead in PaperTradeOrder.objects.filter(live_order=True, strategy=lpt_order.strategy):
                pt_order_dead.live_order = False
                pt_order_dead.save()

            print(f" Success: Got out of all positions for {lpt_order.strategy}.", file=log)

    # Get all paper trader live orders
    lpt_order_obj = PaperTradeOrder.objects.filter(live_order=True)

    if not lpt_order_obj:
        print("No live paper trader order exist in the database.", file=log)

    now_dt = make_aware(datetime.now())
    now_dt = now_dt.replace(hour=0, minute=0, second=0, microsecond=0)

    # If price_bought of paper_trade order == 0.0 -> set price bought as the company's current close price
    for lpt_order in lpt_order_obj:
        # print(lpt_order)

        company = Company.objects.get(ticker=lpt_order.order.company.ticker)
        # print(company)

        candle_stick = ImmutableData.objects.get(company=company, time_stamp=now_dt)
        # print(candle_stick)

        # print(lpt_order.price_bought)

        if lpt_order.price_bought == 0.0:
            price_bought = candle_stick.close
            # print(candle_stick.time_stamp)
            # print(candle_stick.close)

            try:
                lpt_order.price_bought = price_bought
                lpt_order.save()
                # print(lpt_order)
                print(" Success: price_bought parameter set for live paper trade order. ", file=log)

            except:
                print(" Failed: price_bought parameter not set for live paper trade order. ", file=log)

        else:

            # Evaluate profit / loss of order according to latest company data
            try:

                current_price = candle_stick.close

                pl_diff = 0.0
                percent_diff = 0.0

                if lpt_order.order.order_type == 'B':
                    pl_diff = float(current_price - lpt_order.price_bought)
                    percent_diff = float((pl_diff / lpt_order.price_bought) * 100)

                elif lpt_order.order.order_type == 'S':
                    pl_diff = float((current_price - lpt_order.price_bought) * -1)
                    percent_diff = float((pl_diff / lpt_order.price_bought) * 100)

                # print(current_price)
                # print(lpt_order.price_bought)
                # print(pl_diff)
                # print(percent_diff)
                # print(Orders.objects.get(id=lpt_order.order.id))

                order = Orders.objects.get(id=lpt_order.order.id)
                order.profit_loss = pl_diff
                order.save()

                lpt_order.percentage_change = percent_diff
                lpt_order.save()

                # print(lpt_order)
                print(f" Success: profit_loss parameter set for live paper trade order {order}. ", file=log)
                print(f" Success: percentage_change parameter set for live paper trade order {order}. ", file=log)

            except:
                print(f" Failed: profit_loss parameter not set for live paper trade order {order}. ", file=log)
                print(f" Failed: percentage_change parameter not set for live paper trade order {order}. ", file=log)


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
                        time_stamp=now_dt,
                        quantity=1,
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
