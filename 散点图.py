import matplotlib.pyplot as plt
import scipy
import numpy as np

x=np.random.randn(500)

y=x+np.random.randn(500)*0.5

plt.scatter(x,y,s=5,marker='<')

plt.show()