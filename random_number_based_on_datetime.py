# Packages we need to use
import datetime
import time
import random

# Get a random date
start_date = datetime.date(2020, 1, 1)
actual_date = datetime.date.today()

time_between_dates = actual_date - start_date
days_between_dates = time_between_dates.days
random_number_of_days = random.randrange(days_between_dates)
random_date = start_date + datetime.timedelta(days=random_number_of_days)
#print(random_date)

# Get magical number based on random date generated
unixtime = time.mktime(random_date.timetuple())
print("Magical number: {}".format(unixtime))
