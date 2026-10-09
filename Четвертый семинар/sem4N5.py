import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('BTC_data.csv')
time = list(df['time'])
close = list(df['close'])


plt.figure(figsize=(10, 5))
plt.title('BTC Close Price')
plt.plot(time, close, color = 'black', linewidth = 1, linestyle = '-') 

plt.xlabel('Time')
plt.ylabel('Close')

plt.show()