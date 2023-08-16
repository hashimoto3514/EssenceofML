import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 200)
y1 = x**2
y2 = (x - 2)**2

plt.plot(x, y1, color="k")
plt.plot(x, y2, color="k", linestyle="--")
plt.show()
