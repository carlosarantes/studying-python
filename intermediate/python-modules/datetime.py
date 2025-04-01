import datetime

mytime = datetime.time(2,20,2,3)

mytime.minute

mytime.hour

type(mytime)

today = datetime.date.today()

today.ctime()


## --------------

from datetime import datetime

mydatetime = datetime(2021, 10, 3,14,20, 1)

mydatetime.replace(year=2022)

## --------------


from datetime import date

date1 = date(2021,11,3)
date2 = date(2020,11,1)

print(date1 - date2)