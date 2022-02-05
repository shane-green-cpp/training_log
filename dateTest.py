import datetime
date = datetime.date(2021, 12, 24)
today = datetime.date.today()

print(date)
print(today)

if today==date:
    print('beans')
else:
    print('fuck')