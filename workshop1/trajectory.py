from numpy import *
from pylab import *
from math import pi
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle
from matplotlib import animation
import argparse

parser = argparse.ArgumentParser(description="Working with Trajectories")
parser.add_argument('-p','--path', help="line or spline")
args = parser.parse_args()


plt.style.use('dark_background')
rcParams['figure.figsize'] = (10.0, 6.0)


def point_to_point_traj(x1, x2, v1, v2, delta_t):
  t = np.linspace(0, delta_t, 100)  
  a0 = x1
  a1 = v1
  a2 = (3*x2 - 3*x1 - 2*v1*delta_t - v2 * delta_t) / (delta_t**2)
  a3 = (2*x1 + (v1 + v2) * delta_t  - 2 * x2) / (delta_t**3)

  polynomial = a0 + a1 * t + a2 * t**2 + a3 * t**3
  derivative = a1 + 2*a2 * t + 3 * a3 * t**2
  return polynomial, derivative


def piecewise2D (X,Y, Vx, Vy, T):
    theta_x, theta_y, dx, dy = [], [], [], []

    for i in range(len(P)-1):          
        theta_xi, dxi = point_to_point_traj(X[i], X[i+1], Vx[i], Vx[i+1], T[i+1] - T[i])
        theta_yi, dyi = point_to_point_traj(Y[i], Y[i+1], Vy[i], Vy[i+1], T[i+1] - T[i])

        theta_x += theta_xi.tolist()
        theta_y += theta_yi.tolist()
        dx += dxi.tolist()
        dy += dyi.tolist()

        plot(theta_xi, theta_yi)
    return theta_x, theta_y, dx, dy


# Plotting
def plot_points():
    plot(X,Y, '--')
    plot(X,Y, 'o')
    quiver(X,Y, Vx, Vy, color='r')
    
# Speed
def plot_speed():
    speed = np.sqrt(np.array(dx)**2 + np.array(dy)**2)
    plot(speed)
    

##### Requirements for the trajectory
if (args.path == 'line'):
    # Waypoints
    p1 = [-5.,-7]
    p2 = [10,-7]
    p3 = [9,-4]
    p4 = [4,-2]
    p5 = [3,0]
    p6 = [3,6]
    p7 = [0,6]
    p8 = [0,0]
    p9 = [3,0]
    p10 = [3,10]
    p11 = [9,10]

#     # Velocities
#     v1 = [1,0]
#     v2 = [0,1]
#     v3 = [-1,0]
#     v4 = [-0.5,0]
#     v5 = [0,1]
#     v6 = [-1,0]
#     v7 = [0,-1]
#     v8 = [1,0]
#     v9 = [0,1]
#     v10 = [1,0]
#     v11 = [0.0001,0]
    v1=v2=v3=v4=v5=v6=v7=v8=v9=v10=v11 = [0,0]


    # Time
    t1 = 0
    t2 = 1
    t3 = 2
    t4 = 3
    t5 = 4
    t6 = 5
    t7 = 6
    t8 = 7
    t9 = 8
    t10= 9
    t11= 10

    # Convert the initial conditions to a vector form
    P = np.vstack((p1, p2, p3, p4, p5,p6,p7,p8,p9,p10,p11))
    V = np.vstack((v1, v2, v3, v4, v5,v6,v7,v8,v9,v10,v11))
    T = [t1, t2, t3, t4, t5,t6,t7,t8,t9,t10,t11]

if (args.path == 'spline'):
    p1 = [-5.,-7]
    #p2 = [10,-7]
    p3 = [10,-4.5]
    #p4 = [4,-2]
    p5 = [3,0]
    #p6 = [3,6]
    p7 = [2,6]
    #p8 = [0,0]
    p9 = [2,0]
    p10 = [3,10]
    p11 = [9,10]
    
    v1 = [2,0]
    v3 = [-2,2]
    v5 = [0,1]
    v7 = [-2,0]
    v9 = [3,1]
    v10 = [1,0]
    v11 = [0.001,0]
    
    
    t1 = 0
    t3 = 4
    t5 = 8
    t7 = 12
    t9 = 16
    t10 = 18
    t11 = 22
    
    P = np.vstack((p1, p3, p5, p7, p9, p10, p11))
    V = np.vstack((v1, v3, v5, v7, v9, v10, v11))
    T = [t1, t3, t5, t7, t9, t10, t11]


X, Y = P[:,0], P[:,1]
Vx, Vy = V[:,0], V[:,1]


    
plot_points()
# Plot the trajectory that passes trhough the desired waypoints
theta_x, theta_y, dx, dy = piecewise2D(X,Y, Vx, Vy, T)

plot_points()
# Plot speed
plot_speed()


fig, ax = plt.subplots()


def animate(t):
    ax.clear()
    ax.add_patch(Rectangle((4, -1), 2, 10,fill=True, color='g',alpha=0.5, lw=0))
    ax.add_patch(Rectangle((0.5, 2), 2, 3,fill=True, color='b',alpha=0.5, lw=0))
    ax.add_patch(Rectangle((-6, -5), 15, 1,fill=True, color='g',alpha=0.5, lw=0))
    ax.add_patch(Rectangle((8, 0), 2, 5,fill=True, color='g',alpha=0.5, lw=0))
    ax.add_patch(Rectangle((-4, -3), 2, 8,fill=True, color='g',alpha=0.5, lw=0))
    # Path
    ax.plot(theta_x, theta_y, 'b--')
    
    # Initial conditions
    ax.plot(X,Y, 'go')
    ax.quiver(X,Y, Vx, Vy, color='0.4', scale=20)
        
    # Dynamic position
    ax.plot(theta_x[t], theta_y[t], 'ro', markersize=10)
       
    # Velocity vector
    ax.quiver([theta_x[t]], [theta_y[t]], [dx[t]], [dy[t]], color='r', units='xy', scale=10/np.linalg.norm([theta_x[t], theta_y[t]]))
    

anim = animation.FuncAnimation(fig, animate, frames=int(len(theta_x)/1), interval=25)

anim.save(f"trajectory-{args.path}.mp4", dpi=300)

