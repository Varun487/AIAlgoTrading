from datetime import datetime
log = open("/home/app/microservice/cron/cronlog", "a+")
print(f'{datetime.now()}: Work on cron job.', file=log)
print("New line bro.", file=log)
