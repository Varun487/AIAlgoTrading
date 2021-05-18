from datetime import datetime
from datetime import timedelta


DATE_FORMAT = '%Y/%m/%d'

def daterange(start, end):
      def convert(date):
            try:
                  date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
                  return date.date()
            except TypeError:
                  return date

      def get_date(n):
            return datetime.strftime(convert(start) + timedelta(days=n), '%Y-%m-%d %H:%M:%S')

      days = (convert(end) - convert(start)).days
      for n in range(0, days):
            yield get_date(n)


start = '2021-05-14 00:00:00'
end = '2021-05-20 00:00:00'
print list(daterange(start, end))

