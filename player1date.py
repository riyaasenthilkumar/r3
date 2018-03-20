import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

dr = pd.date_range(start='2015-07-01', end='2015-07-31')
df = pd.DataFrame()
df['Date'] = dr

cal = calendar()
holidays = cal.holidays(start=dr.min(), end=dr.max())

df['Holiday'] = df['Date'].isin(holidays)
print df
