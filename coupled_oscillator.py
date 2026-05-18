import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# PARAMETERS

n = int(input("Enter the number of masses: "))        
mode_no = int(input("Enter the mode number (1 to n): "))# number of masses
L = 10              # total length
A = 0.4             # oscillation amplitude
k = 10               # spring constant
m = 1               # mass
       # mode number (1 to n)
dt = 0.03


# EQUILIBRIUM POSITIONS

eq_x = np.linspace(0, L, n)
y = np.zeros(n)

# -----------------------------
# CREATING COUPLING MATRIX
# -----------------------------
K = np.zeros((n, n))

for i in range(n):

    K[i][i] = 2

    if i > 0:
        K[i][i - 1] = -1

    if i < n - 1:
        K[i][i + 1] = -1

# -----------------------------
# EIGENVALUES / EIGENVECTORS
# -----------------------------
eigvals, eigvecs = np.linalg.eig(K)

# sort them properly
idx = np.argsort(eigvals)

eigvals = eigvals[idx]
eigvecs = eigvecs[:, idx]

# selected mode
p = mode_no - 1

mode_shape = eigvecs[:, p]

# angular frequency
omega = np.sqrt((k/m) * eigvals[p])

# -----------------------------
# PLOT
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 3))

ax.set_xlim(-1, L + 1)
ax.set_ylim(-1.5, 1.5)

line, = ax.plot([], [], 'o-', ms=8)

time = 0

# -----------------------------
# INITIALIZATION
# -----------------------------
def init():

    line.set_data(eq_x, y)

    return line,

# -----------------------------
# ANIMATION FUNCTION
# -----------------------------
def animate(frame):

    global time

    time += dt

    x = []

    for i in range(n):

        displacement = A * mode_shape[i] * np.cos(omega * time)

        x.append(eq_x[i] + displacement)

    line.set_data(x, y)

    return line,

# -----------------------------
# ANIMATION
# -----------------------------
ani = FuncAnimation(
    fig,
    animate,
    init_func=init,
    interval=20,
    blit=True
)

plt.title(f"Normal Mode {mode_no}")
plt.show()
