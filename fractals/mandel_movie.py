import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib import animation
import time

# some interesting places in the set
# http://www.nahee.com/Derbyshire/manguide.html

N = 500
nIts = 25
nZooms = 30
x0=0
y0=-1

movie = np.zeros([N,N,nZooms])

x = np.linspace(-2,1,N,dtype=np.float128)
y = np.linspace(-1,1,N,dtype=np.float128)
X,Y = np.meshgrid(x,y)
c = X + 1j*Y
z = 0*c
for i in range(nIts):
    z = z**2 + c

mask = np.abs(z) < 1
z[z>1]=0
z[np.isnan(z)]=0
movie[:,:,0] = mask


# plotting stuff
for j in range(1,nZooms):
    h=1./(2**j)
    print "Plot number ", j
    x = x0+h*np.linspace(-1,1,N,dtype=np.float128)
    y = y0+h*np.linspace(-1,1,N,dtype=np.float128)
    X,Y = np.meshgrid(x,y)
    c = X + 1j*Y
    z = 0*c
    for i in range(nIts):   # more iterations at deeper levels??
        z = z**2 + c

    mask = np.abs(z) < 1
    z[z>1]=0
    z[np.isnan(z)]=0
    movie[:,:,j] = mask

fig = plt.figure()

for j in range(nZooms):
    name = "image%d.png" % j
    plt.imshow(movie[:,:,j], cmap = 'RdBu')
    plt.gray()
    plt.axis('equal')
    plt.axis('off')
    # plt.show()
    fig.savefig(name)
    time.sleep(1)


# what is this painfully slow?!
## def animate(i):
##     frame = movie[:,:,i]
##     cont = plt.imshow(frame)
##     #cont = plt.contourf(X,Y,z)
##     return cont

## anim = animation.FuncAnimation(fig,animate,frames=nZooms)
## plt.imshow(mask, cmap = 'RdBu')
## plt.gray()
## plt.show()
