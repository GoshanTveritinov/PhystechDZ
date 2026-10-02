import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data.csv')

counts = df['Species'].value_counts()
print(counts)

x = sum(df['PetalLengthCm'] <= 1.2)
y = sum( (df['PetalLengthCm'] > 1.2) & (df['PetalLengthCm'] <= 1.5) )
z = sum(df['PetalLengthCm'] > 1.5)

fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(10, 6))

axes[0].pie((x, y, z), labels = ['small', 'medium', 'big'], radius = 1.5, explode = [0.1, 0.05, 0.04])
axes[1].pie(counts, labels = counts.index, radius = 1.5, explode=[0.03, 0.03, 0.03])

plt.subplots_adjust(wspace=1)
plt.show()

