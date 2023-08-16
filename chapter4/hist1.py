import numpy as np
import matplotlib.pyplot as plt

np.random.seed(200)
l = []

for _ in range(1000):
    l.append(np.random.randint(1,7,size = 20).sum())

plt.hist(l,20,color='gray')
plt.show()