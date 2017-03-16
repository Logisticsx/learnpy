import matplotlib.pyplot as plt

import numpy as np

mu = 100

sigma = 20

x = mu + sigma * np.random.randn(20000)

plt.hist(x, bins=100, color='green', normed=True)

plt.show()
