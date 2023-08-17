import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return x**2 + y**2 + x*y + 2*x + 4*y 


x = np.linspace(-6, 5, 300)
y = np.linspace(-6, 5, 300)
xmesh, ymesh = np.meshgrid(x, y)
z = f(xmesh.ravel(), ymesh.ravel()).reshape(xmesh.shape)
level = [ i for i in range(-5,0)]
print(level)
plt.ylim([-6,4])
plt.contour(x, y, z, colors="k", levels=level)
plt.show()
