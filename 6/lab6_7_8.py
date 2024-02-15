import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.colors import LightSource
import sys
def my_spher(N = 20, R=2):
  # parametric
  u = np.linspace(0, 2 * np.pi, N)
  v = np.linspace(0, np.pi, N)
  x = R * np.outer(np.cos(u), np.sin(v))
  y = R * np.outer(np.sin(u), np.sin(v))
  z = R * np.outer(np.ones(np.size(u)), np.cos(v))
  return x,y,z
xs = np.linspace(-20, 80, 100)
ys = np.linspace(-20, 50, 100)
X1, Y1 = np.meshgrid(xs, ys)
a1=np.pi/5#угол к гаризонту
v0=10#начальная скорость
g=10#ускорение свободного падения
alf = 24/180*np.pi#  угол между соседними точками окружности
r = 5 # радиус цилиндра 
Rz=[[np.cos(alf), np.sin(alf), 0,0],[-np.sin(alf),  np.cos(alf), 0,0],[0, 0, 1,0],[0,0,0,1]]
Ry=np.array([[ np.cos(a1), 0,  -np.sin(a1),0],[0,1, 0,0],[ np.sin(a1), 0, np.cos(a1),0],[0,0,0,1]])#матрица поворота относительно Yо
# Rx=np.array([[1, 0, 0, 0],[0, np.cos(a1), -np.sin(a1),0],[0, np.sin(a1), np.cos(a1),0],[0,0,0,1]]) # почему - то не работает 
P0 = [2,0, 10,1]
O0 = [r/1.44 ,0, 0,1]
P=[O0]#1 основание
O0 = [r/2 ,0, 0,1]
P_new=[O0]#1 основание
Tp = np.array([[1, 0, 0,0],[0 ,1 ,0,0],[0,0,1,0],[ P0[0],P0[1],P0[2] , 1]])# высота пушки
for  n in np.linspace( 0,360, 360 // 10):
    P += [np.dot(P[-1][:],Rz).tolist()]# создаем список координат окружности 
    P_new += [np.dot(P_new[-1][:],Rz).tolist()]
# Q=np.eye(4) #необязательно 
P=np.array(P)# делаем массив координат окружности
P_new=np.array(P_new)
Q=Tp.dot(Ry)# матрица преобразований для пушки
# print(Q,"...")
P_new=P_new.dot(Q)# верхнее основание пушки повернутое на угол к горизонту 
# print(np.size(P))
P=P.dot(Ry)# нижнее основание пушки повернутое на угол к горизонту 
Pr2=[]
for i in range(30):
#     ax.plot3D([P[i,0],P_new[i,0]],[P[i,1],P_new[i,1]],[P[i,2], P_new[i,2]],'b')
    Pr2+=[P[i,:]]
    Pr2+=[P_new[i,:]]
Pr2+=[P[0,:]]
Pr2+=[P_new[0,:]]

Pr2=np.array(Pr2)# делаем матрицу закраски ТРЕУГОЛЬНИКАМИ , можно квадратиками 

fig = plt.figure()
ax = fig.add_subplot(projection='3d')# создаем среду 

ax.plot3D(P[:,0],P[:,1],P[:,2])
ax.plot3D(P_new[:,0],P_new[:,1],P_new[:,2])# рисуем основания пушки 
for i in range(30):
    ax.plot_trisurf(Pr2[i:(i+3),0],Pr2[i:(i+3),1],Pr2[i:(i+3),2],  linewidth = 0.2,
                         antialiased = True, shade=True ,alpha=0.5,color='gray')# цвет+прозрачность пушки
light_1 = LightSource(azdeg=300, altdeg=45)    
Z1=X1-X1-5
ax.plot_surface(X1, Y1, Z1,rcount=40, ccount=40,
                      linewidth=0.5, color='g',alpha = 0.45,lightsource=light_1)
X,Y,Z = my_spher()
vz = v0/np.sin(a1)
vy = v0/np.cos(a1)
ax.set_xlim(-10, 80)
ax.set_ylim(-10, 40)
ax.set_zlim(-2, 35)
ax.view_init(elev=0, azim=90)
# Begin plotting.
wframe = None
tstart = time.time()
XYZ = np.hstack((X.reshape(-1,1)+2,Y.reshape(-1,1)+2,Z.reshape(-1,1)+2,np.ones((X.size,1))))
print(XYZ.shape)
for k in range(30):#np.linspace(0, 180. / np.pi, 100):
    
    t=k/50
    vz = vz-g*t
    vy = vy
    T=np.array([[1, 0, 0, 0],[0 ,1 ,0, 0],[0, 0, 1, 0],[  vy*t, 0,  vz*t,1]])



    XYZ = XYZ.dot(T)
    print(XYZ)
    # If a line collection is already remove it before drawing.
    if wframe:
        wframe.remove()
    # Generate data.

    # Plot the new wireframe and pause briefly before continuing.
    
    wframe = ax.plot_surface(XYZ[:,0].reshape(-1,10), XYZ[:,1].reshape(-1,10), XYZ[:,2].reshape(-1,10),color='black',lightsource=light_1)
    #plt.pause(.001)
    #plt.show()
    plt.savefig('filename'+str(k)+'.png')
    for i in XYZ[:,2]:
        if i<-2:
            sys.exit(0)

plt.show()