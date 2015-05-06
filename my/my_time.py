#!/usr/bin/env python

import time
import datetime

# time
print time.localtime(time.time())
print time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(time.time()))

# interval days between 2 dates
start_date = datetime.datetime(2009, 11, 30)
current_date = datetime.datetime.now()
print str((current_date - start_date).days) + " days"

# get a date after some days
future_date = start_date + datetime.timedelta(days=2000)
print future_date.date()