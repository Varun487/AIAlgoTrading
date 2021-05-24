import sys

# Adding a path for easier imports
sys.path.append('/home/app/microservice')

from datetime import datetime, timedelta
from django.utils.timezone import make_aware

# Opening log file
log = open("/home/app/microservice/cron/cronlog", "a+")
print(f'{datetime.now()}: CRON JOB EXECUTED', file=log)

from django import setup
from django.conf import settings

from AITradingPlatform.AITradingPlatform import AITradingPlatform_defaults

# Configuring settings to run a stand alone django application
settings.configure(AITradingPlatform_defaults)

# To initialize the new app
setup()
print(' Django stand alone app setup successful!', file=log)

# Get required models
from AITradingPlatform.DataFeeder.models import Company, ImmutableData
from AITradingPlatform.DataFeeder.utils import get_data_on_demand

try:

    # for all companies in db which use Yahoo finance to source data
    for company_obj in Company.objects.filter(data_provider='Yahoo'):

        all_sourced_data = ImmutableData.objects.order_by('time_stamp').filter(company=company_obj)

        if len(all_sourced_data) > 0:
            latest_dt = all_sourced_data[len(all_sourced_data) - 1].time_stamp
            latest_dt -= timedelta(days=10)

            now_dt = make_aware(datetime.now())
            now_dt = now_dt.replace(hour=0, minute=0, second=0, microsecond=0)

            collected_data, data_not_found = get_data_on_demand([company_obj.ticker], 'Yahoo', latest_dt, now_dt, 'daily', 'year1month1')

            new_sourced_data = ImmutableData.objects.order_by('time_stamp').filter(company=company_obj)

            print(f" Collected data for {company_obj.ticker} from {latest_dt} to {now_dt} and pushed to DB.", file=log)
        else:
            print(f" No data for {company_obj.ticker} in DB. No data sourced.", file=log)

    # remove added path
    sys.path.pop()

    print(" Execution success!", file=log)

except Exception as e:
    print(' ' + str(e), file=log)

    exception_type, exception_object, exception_traceback = sys.exc_info()
    filename = exception_traceback.tb_frame.f_code.co_filename
    line_number = exception_traceback.tb_lineno

    print(" Exception type: ", exception_type, file=log)
    print(" File name: ", filename, file=log)
    print(" Line number: ", line_number, file=log)
