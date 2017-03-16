import matplotlib.pyplot as plt
import scipy
import numpy as np


y=[20,10,30,25,15,9]

index=np.arange(6)

plt.bar(left=index,height=y,color='blue',width=0.5)

plt.show()
