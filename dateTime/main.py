import datetime
import time
import pygame


date = datetime.date(2023, 10, 1)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

print(date)
print(today)
print(time)
print(now)

target_datetime = datetime.datetime(2023, 10, 1, 12, 30, 0)
current_datetime = datetime.datetime.now()

if target_datetime > current_datetime:
    print("target datetime is in the future")
elif target_datetime < current_datetime:
    print("target datetime is in the past")

# -----------------------------------------------------------
print(" -----------------------------------------------------------")
# --------------------------------------------------------
