import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
A=1
w=2
t=0
x=[]
phi=[]
y=[]
k=0.5
l=60
reached=[]
for i in range(0,50):
    y.append(0)
    x.append(i * l/50)
    phi.append(k*x[i])
    reached.append(0)
    
ax.set_ylim(-3, 3)
ax.set_xlim(-10,60)
ax.set_xlabel('Position')
ax.set_ylabel('height')
reached[0] = 1
line,= ax.plot(x, y, 'ro',ms=3) 

def animate(i):
    global t, x, y
    t += 0.1
    for j in range(0, 50):
        if reached[j] == 0:
            
           phi[j] = k*x[j]-w*t
        if phi[j] > 0 and reached[j] == 0:
            reached[j] = 1
        if reached[j] == 1:
           x[j] = A*np.cos(w*t-phi[j])+phi[j]/k
           

    line.set_data(x, y)
    
ani = FuncAnimation(fig, animate, frames=100, interval=100)
        
ax.set_title('Longitudinal Wave Propagation')
plt.grid()
plt.show()