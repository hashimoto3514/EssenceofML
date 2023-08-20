import polyreg
import linearreg
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[1,2],
              [2,3],
              [3,4],
              [4,5],
              [5,6],
              [6,7],
              [7,9]])
print(X.shape[1])
labels = np.array([0,1,2,0,1,2,0])

cluster_centers = np.array([[1,1],
                            [2,2],
                            [3,3]])

p = X[:,:,np.newaxis]
#print(p)
q = cluster_centers.T[np.newaxis,:,:]
#print(q)

r = (p-q)**2
s = r.sum(axis=1)
#print(s)

s_ = s.argmin(axis=1)
#print(s_)