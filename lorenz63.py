import numpy as np
import matplotlib.pyplot as plt #2d plot
from mpl_toolkits.mplot3d import Axes3D #3d plot
import csv 

#define setting
dt = 0.01
step = 10000

#define parameters
b=8.0/3.0
r=28.0 #case1
#r=14.0 #case2
#r=1.0 #case3
s=10.0

#define matrix
xt = np.empty(step+1)
yt = np.empty(step+1)
zt = np.empty(step+1)
data = np.empty(3)

f=open('data.csV','w')
writer = csv.writer(f,lineterminator='\n')

#define initial
xt[0] = 5.81797312611
yt[0] = -5.03517042808 
zt[0] =  25.0706173063

# Forward time step
for i in range(step):
    xt[i + 1] = xt[i] -s*(xt[i]-yt[i])*dt
    yt[i + 1] = yt[i] +(-yt[i]-xt[i]*zt[i]+r*xt[i])*dt
    zt[i + 1] = zt[i] +(xt[i]*yt[i]-b*zt[i])*dt
    data[0]=xt[i+1] #for output xt
    data[1]=yt[i+1] #for output yt
    data[2]=zt[i+1] #for output zt
    writer.writerow(data)

f.close()

#2dplot
plt.figure(figsize=(18, 6), dpi=200)
plt.subplot(131)
plt.xlabel( 'x' )  #x name
plt.ylabel( 'y' )  #y name
plt.xlim(-30.0, 30.0) #x limit
plt.ylim(-30.0, 30.0) #y limit
plt.plot(xt,yt, color="black", linewidth=0.5)

plt.subplot(132)
plt.xlabel( 'x' )  #x name
plt.ylabel( 'z' )  #y name
plt.xlim(-30.0, 30.0) #x limit
plt.ylim(0.0, 60.0) #y limit
plt.plot(xt,zt, color="black", linewidth=0.5)

plt.subplot(133)
plt.xlabel( 'y' )  #x name
plt.ylabel( 'z' )  #y name
plt.xlim(-30.0, 30.0) #x limit
plt.ylim(0.0, 60.0) #y limit
plt.plot(yt,zt, color="black", linewidth=0.5)
plt.savefig("output1.png", dpi=200)

#3d plot
fig = plt.figure(figsize=(12, 12), dpi=200)
ax = Axes3D(fig)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(-30.0, 30.0) #x limit
ax.set_ylim(-30.0, 30.0) #y limit
ax.set_zlim(0.0, 60.0) #z limit
ax.plot3D(xt,yt,zt, color="black", linewidth=0.5)
plt.savefig("output2.png", dpi=200)
plt.show()
