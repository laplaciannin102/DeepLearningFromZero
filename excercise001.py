# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# データの作成
x = np.arange(0, 6, 0.25)
y = np.sin(x)

plt.plot(x, y)
plt.show()