import sys

# Adding a path for easier imports
sys.path.append('/home/app/microservice')

from datetime import datetime

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
from AITradingPlatform.DataFeeder.models import Company

try:
    # print all company objects
    print(" " + str(Company.objects.all()), file=log)

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
