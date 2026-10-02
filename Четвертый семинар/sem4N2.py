import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, axes = plt.subplots(nrows = 2, ncols = 2, figsize=(10, 10))

pos = 0
scale = 10
size = [100, 1000, 10000, 100000]
for i in range (len (size)):
    values = np.random.normal(pos, scale, size[i])
    axes[i//2, i%2].hist(values, 100)

plt.show()



