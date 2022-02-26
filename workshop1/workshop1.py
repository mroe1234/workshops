from numpy import *
from pylab import *
from math import pi
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d

import argparse

parser = argparse.ArgumentParser(description="Working with Trajectories")
parser.add_argument('-s','--shape', help="oval, flower or helix")
parser.add_argument('-w','--wind', action='store_true', help="enables wind disturbances")
args = parser.parse_args()



def sense(x):
    return x

def simulate(Δt, x, u):
    MAX = 0.1
    MIN = -0.1
    if args.wind:
        wind = [np.random.uniform(MIN,MAX), np.random.uniform(MIN,MAX),0]
    else:
        wind = 0
    x += Δt * u +wind
    return x

def oval(t,y):
    #Oval
#    ux = -4*sin(t-0.5)
#    uy = 2*cos(t)
    ux = 2*(cos(2*t-0.5) - 2*sin(2*t-0.5))
    uy = 2*(2*cos(2*t) + sin(2*t))
    return array([ux,uy,0])

def flower(t,y):
    #flower
    #r=3sin(5theta)
    #ux = 4*cos(4*t)
    #uy = cos(t)
    xerr = 0
    yerr = 0
    if args.wind:
        #adjust for disturbances
        xerr = 5*(cos(t-0.1)*(3*sin(5*(t-0.1))+2) - (x_log[-1][0]))
        yerr = 5*(sin(t-0.1)*(3*sin(5*(t-0.1))+2) - (x_log[-1][1]))
    ux = 15*cos(t)*cos(5*t) - sin(t)*(5 + 3*sin(5*t)) + xerr
    uy = 15*cos(5*t)*sin(t) + cos(t)*(5 + 3*sin(5*t)) + yerr
    return array ([ux,uy,0])

def helix(t,y):
    #helix
    ux = 10*cos(t)
    uy = 10*sin(t)
    uz = 50
    return array([ux,uy,uz])


def control(t, y,shape):
    ### WRITE YOUR CONTROL POLICY HERE:
    #ux = -sin(t)
    #uy = cos(t)
    #360/30 = 12
    #2pi / 12 = ~0.5
#    ux = 4*cos(t-0.5)
#    uy = 2*sin(t)
#    return array([ux, uy])
    if shape == 'oval':
        return oval(t,y)
    if shape == 'flower':
        return flower(t,y)
    if shape =='helix':
        return helix(t,y)
        
    return oval(t,y)

def animate(t):
    ax.clear()
    # Path
    if (args.shape == "helix"):
        ax.plot3D(x_log[:,0], x_log[:,1],x_log[:,2], 'r--')
    else:
        plot(x_log[:,0], x_log[:,1], 'r--')


    # Initial conditions
    if (args.shape == "helix"):
        ax.plot3D(x_log[int(t),0], x_log[int(t),1],x_log[int(t),2], 'bo')
    else:
        plot(x_log[int(t),0], x_log[int(t),1], 'bo')


tf = 20.
Δt = 0.1    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval
# Initial conditions
x = array([2., 1.,0.])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = control(t, y,args.shape)
    #u1 = control(t, y[1],'square')
    x = simulate(Δt, x, u)
    #x[1] = simulate(Δt, x[1], u1)
    x_log.append(copy(x))
x_log = array(x_log)
#grid()
fig = plt.figure()

if (args.shape == "helix"):
    ax = fig.add_subplot(1,2,1, projection='3d')
    ax.plot3D(x_log[:,0], x_log[:,1],x_log[:,2])
    ax = fig.add_subplot(1,2,2,projection='3d')
else:
    plot(x_log[:,0], x_log[:,1])
    #plot (x_log[:,0,0], x_log[:,0,1])
    #plot (x_log[:,1,0], x_log[:,1,1])
    fig, ax = plt.subplots()
anim = animation.FuncAnimation(fig, animate, frames=len(time), interval=60)
#anim.to_jshtml()
plt.show()

