import datetime
import time


my_date = [str(datetime.date.today().year), str(datetime.date.today().month), str(datetime.date.today().day)]
print("-".join(my_date))

print(datetime.date.isoformat(datetime.date.today()))
print(time.strftime('%Y%m%d %I:%M%p'))
print(time.strftime("%A %p"))
