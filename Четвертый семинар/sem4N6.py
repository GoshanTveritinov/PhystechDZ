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


x = np.linspace(0, 1457, 1457)
closeagain = list(df['close'])
z = np.polyfit(x, closeagain, 8) 
p = np.poly1d(z)

plt.plot(x, p(x), color = 'red')


plt.show()