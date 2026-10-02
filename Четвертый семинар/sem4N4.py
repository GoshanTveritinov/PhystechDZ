import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

sl = list(df['SepalLengthCm'])
sw = list(df['SepalWidthCm'])
#pl = list(df['PetalLengthCm'])
#pw = list(df['PetalWidthCm'])

for i in range(0, 150):
    plt.plot(sl[i], sw[i], marker="o", color = "red")

plt.show()