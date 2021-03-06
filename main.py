import numpy as np
from pandas import read_csv
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize


df = read_csv("kshdeath.csv", parse_dates=['date'])
dates = df["date"]
df = df.drop(columns=["date"])
age_intervals = list(df.columns)

#normalized_df = (df-df.mean())/df.std()
normalized_df = df
# we are assuming dates are ordered
#plt.pcolormesh(normalized_df.T,norm=Normalize(0,3))
plt.pcolormesh(normalized_df.T)
c = np.arange(1,len(dates)+1,52)
x_dates = dates[c]
plt.xticks(c, x_dates.dt.strftime("%Y"), rotation='vertical')
plt.yticks(np.arange(0.5, len(age_intervals), 1), age_intervals)
plt.colorbar()
plt.show()