import matplotlib
import matplotlib.pyplot as plt

x=0
t=0
y=0
dt=1
vx=20
vy=30
g=9.8
x_positions = []
times = []
y_positions = []
x_positions.append(0)
y_positions.append(0)
times.append(0)
for i in range(0, 100):
    t = t + dt
    x = x + vx * dt
    vy = vy - g * dt
    y = y + vy*dt
    
    if y < 0:
        break
    x_positions.append(x)
    times.append(t)
    y_positions.append(y)
    
plt.plot(times, x_positions, label="x")
plt.plot(times, y_positions, label="y")
plt.xlabel("Time")
plt.ylabel("Position")
plt.title("Position vs Time")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
