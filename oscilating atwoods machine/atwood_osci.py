import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =====================================================
# Parameters
# =====================================================

g = 9.8
m1 = 1
m2 = 2

# =====================================================
# Equations of motion
# =====================================================

def system(t, y):

    r, r_dot, theta, theta_dot = y

    # radial acceleration
    r_2dot = (
        g * m1 * np.cos(theta)
        - (g * m1 + g * m2)
        + m1 * r * theta_dot**2
    ) / (m1 + m2)

    # angular acceleration
    theta_2dot = (
        -g * np.sin(theta)
        - 2 * r_dot * theta_dot
    ) / r

    return [
        r_dot,
        r_2dot,
        theta_dot,
        theta_2dot
    ]

# =====================================================
# Initial conditions
# =====================================================

y0 = [
    1.0,   # r(0)
    0.0,   # r_dot(0)
    0.4,   # theta(0)
    0.0    # theta_dot(0)
]

# =====================================================
# Solve ODE
# =====================================================

t_eval = np.linspace(0, 20, 4000)

sol = solve_ivp(
    system,
    (0, 20),
    y0,
    t_eval=t_eval
)

# =====================================================
# Extract solution
# =====================================================

r = sol.y[0]
theta = sol.y[2]

# =====================================================
# Geometry
# =====================================================

# pulley positions
left_pulley_x = -1
right_pulley_x = 1
pulley_y = 0

# pendulum bob coordinates
x1 = left_pulley_x + r * np.sin(theta)
y1 = pulley_y - r * np.cos(theta)

# counterweight coordinates
x2 = np.full_like(r, right_pulley_x)
y2 = -(2 - r)

# =====================================================
# Figure setup
# =====================================================

fig, ax = plt.subplots(figsize=(7, 7))

ax.set_xlim(-3, 3)
ax.set_ylim(-4, 2)

ax.set_aspect('equal')

ax.set_title("Oscillating Atwood Machine")

ax.grid()

# =====================================================
# Artists
# =====================================================

# strings
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [], lw=2)
top_rope, = ax.plot([], [], lw=2)

# masses
bob1, = ax.plot([], [], 'o', markersize=15)
bob2, = ax.plot([], [], 's', markersize=15)

# trajectory
trail, = ax.plot([], [], lw=1)

# pulleys
ax.plot(left_pulley_x, pulley_y, 'ko', markersize=8)
ax.plot(right_pulley_x, pulley_y, 'ko', markersize=8)




# =====================================================
# Initialization
# =====================================================

def init():

    line1.set_data([], [])
    line2.set_data([], [])
    top_rope.set_data([], [])

    bob1.set_data([], [])
    bob2.set_data([], [])

    trail.set_data([], [])

    return (
        line1,
        line2,
        top_rope,
        bob1,
        bob2,
        trail
    )

# =====================================================
# Animation update
# =====================================================

def update(frame):

    # pendulum string
    line1.set_data(
        [left_pulley_x, x1[frame]],
        [pulley_y, y1[frame]]
    )

    # counterweight string
    line2.set_data(
        [right_pulley_x, x2[frame]],
        [pulley_y, y2[frame]]
    )

    #top rope
    top_rope.set_data(
    [left_pulley_x, right_pulley_x],
    [pulley_y, pulley_y]
    )

    # masses
    bob1.set_data(
        [x1[frame]],
        [y1[frame]]
    )

    bob2.set_data(
        [x2[frame]],
        [y2[frame]]
    )

    # trajectory trail
    trail.set_data(
        x1[:frame],
        y1[:frame]
    )


    return (
        line1,
        line2,
        top_rope,
        bob1,
        bob2,
        trail
    )

# =====================================================
# Animate
# =====================================================

ani = FuncAnimation(
    fig,
    update,
    frames=len(t_eval),
    init_func=init,
    interval=5,
    blit=True
)
ani.save(
    "oscillating_atwood_machine.mp4",
    writer="ffmpeg",
    fps=60,
    dpi=200
)
plt.show()
