# 17_fstring_dates.py

import datetime

day = datetime.datetime(2021, 11, 20)
print(f"{day} was a {day:%A}")