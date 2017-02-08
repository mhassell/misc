import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

N = 7500
nIts = 50

x = np.linspace(-2,1,N)
y = np.linspace(-1,1,N)

X,Y = np.meshgrid(x,y)

c = X + 1j*Y
z = 0*c

for i in range(nIts):
    print "iter number ", i
    z = z**2 + c

mask = np.abs(z) < 1
z[z>1]=0
z[np.isnan(z)]=0

axes = plt.gca()
axes.set_xlim([-2,1])
axes.set_ylim([-1,1])
# plt.contourf(X,Y,np.abs(z))
plt.imshow(mask, cmap = 'RdBu')
plt.gray()
plt.axis('equal')
plt.axis('off')
plt.show()
