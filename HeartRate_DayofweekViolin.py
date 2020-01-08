import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
import calendar

#File path for csv file created by XML to CSV
filepath = 'XMLtoCSV/health_data.csv'

#Convert csv file to dataframe
df = pd.read_csv(filepath, encoding = 'ISO-8859-1')
#Seperate only heart rate observations
df_heartrate = df[df['type'].str.contains('HeartRate')]

#Convert creation date column to datetime format
df_heartrate['creation_date'] = pd.to_datetime(df_heartrate['creation_date'],
                                               format='%Y-%m-%d %H:%M:%S', utc=True)
df_heartrate['creation_date'] = df_heartrate['creation_date'].dt.tz_convert(None)

#Find integer value of weekday
df_heartrate['weekday'] = df_heartrate['creation_date'].dt.dayofweek
dayofweek = df_heartrate['weekday'].to_numpy()

#Convert integer value of weekday to string represenation
dayofweek_string = []
for i in range(0, len(dayofweek)):
    dayofweek_string.append(calendar.day_name[dayofweek[i]])
df_heartrate['weekday'] = dayofweek_string

#Set index of dataframe as creation date
df_heartrate.set_index('creation_date', inplace=True, drop=True)

#Create and show violin plot
sns.catplot(x='weekday', y='value',
            data=df_heartrate, kind='violin',
            order=['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            inner='quartile')
plt.show()
