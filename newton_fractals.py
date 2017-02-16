import numpy as np
import matplotlib.pyplot as plt

# https://en.wikipedia.org/wiki/Newton_fractal

N = 500
nIts = 500

x = np.linspace(-1,1,N)
y = np.linspace(-1,1,N)
X,Y = np.meshgrid(x,y)

z = X + 1j*Y

#f = lambda z : z**3 - 1
#fp = lambda z : 3*z**2

f = lambda z : np.sin(z)-1
fp = lambda z : np.cos(z)

#f = lambda z : np.cosh(z)-1
#fp = lambda z : np.sinh(z)

for i in range(nIts):
	z = f(z)/fp(z)

fig = plt.figure()
plt.imshow(np.abs(z), cmap = 'RdBu')
#cont = plt.contourf(X,Y,np.abs(z))
plt.show()