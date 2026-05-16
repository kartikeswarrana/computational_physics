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

    r_2dot = (
        g * m1 * np.cos(theta)
        - (g * m1 + g * m2)
        + m1 * r * theta_dot**2
    ) / (m1 + m2)

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
    1.0,
    0.0,
    0.4,
    0.0
]

# =====================================================
# Solve system
# =====================================================

t_eval = np.linspace(0, 20, 5000)

sol = solve_ivp(
    system,
    (0,20),
    y0,
    t_eval=t_eval
)

# =====================================================
# Extract variables
# =====================================================

r = sol.y[0]
r_dot = sol.y[1]

theta = sol.y[2]
theta_dot = sol.y[3]

# =====================================================
# Geometry
# =====================================================

left_pulley_x = -1
right_pulley_x = 1
pulley_y = 0

# pendulum bob
x1 = left_pulley_x + r * np.sin(theta)
y1 = pulley_y - r * np.cos(theta)

# counterweight
x2 = np.full_like(r, right_pulley_x)
y2 = -(2 - r)

# =====================================================
# Figure and subplots
# =====================================================

fig, axs = plt.subplots(1, 3, figsize=(16, 9))

ax1 = axs[0]
ax2 = axs[1]
ax3 = axs[2]

# =====================================================
# LEFT: Physical animation
# =====================================================

ax1.set_xlim(-3, 3)
ax1.set_ylim(-4, 2)

ax1.set_aspect('equal')

ax1.set_title("Oscillating Atwood Machine")

ax1.grid()

# strings
line1, = ax1.plot([], [], lw=2)
line2, = ax1.plot([], [], lw=2)

# masses
bob1, = ax1.plot([], [], 'o', markersize=15)
bob2, = ax1.plot([], [], 's', markersize=15)

# trajectory
trail, = ax1.plot([], [], lw=1)

# pulleys
ax1.plot(left_pulley_x, pulley_y, 'ko', markersize=8)
ax1.plot(right_pulley_x, pulley_y, 'ko', markersize=8)

# =====================================================
# Middle: Radial Phase space
# =====================================================

ax2.set_title(" Radial Phase Space")

ax2.set_xlabel(r"$r$")
ax2.set_ylabel(r"$\dot{r}$")

ax2.grid()

# full phase trajectory
ax2.plot(r, r_dot, alpha=0.3)

# moving point
radial_phase_point, = ax2.plot([], [], 'ro')

# phase trail
radial_phase_trail, = ax2.plot([], [], lw=1)


# =====================================================
# Right: Angular Phase Space
# =====================================================

ax3.set_title("Angular Phase Space")

ax3.set_xlabel(r"$\theta$")
ax3.set_ylabel(r"$\dot{\theta}$")

ax3.grid()

ax3.plot(theta,theta_dot,alpha = 0.3)

angular_phase_point, = ax3.plot([], [], 'ro')

angular_phase_trail, = ax3.plot([], [], lw=1)




# =====================================================
# Initialization
# =====================================================

def init():

    line1.set_data([], [])
    line2.set_data([], [])

    bob1.set_data([], [])
    bob2.set_data([], [])

    trail.set_data([], [])

    radial_phase_point.set_data([], [])
    radial_phase_trail.set_data([], [])

    angular_phase_point.set_data([], [])
    angular_phase_trail.set_data([], [])
    return (
        line1,
        line2,
        bob1,
        bob2,
        trail,
        radial_phase_point,
        radial_phase_trail,
        angular_phase_point,
        angular_phase_trail
    )

# =====================================================
# Animation update
# =====================================================

def update(frame):

    # -------------------------
    # Physical system
    # -------------------------

    line1.set_data(
        [left_pulley_x, x1[frame]],
        [pulley_y, y1[frame]]
    )

    line2.set_data(
        [right_pulley_x, x2[frame]],
        [pulley_y, y2[frame]]
    )

    bob1.set_data(
        [x1[frame]],
        [y1[frame]]
    )

    bob2.set_data(
        [x2[frame]],
        [y2[frame]]
    )

    # pendulum trajectory
    trail.set_data(
        x1[:frame],
        y1[:frame]
    )

    # -------------------------
    # Phase space
    # -------------------------

    radial_phase_point.set_data(
        [r[frame]],
        [r_dot[frame]]
    )

    radial_phase_trail.set_data(
        r[:frame],
        r_dot[:frame]
    )
    
    angular_phase_point.set_data(
        [theta[frame]],
        [theta_dot[frame]]
    )

    angular_phase_trail.set_data(
        theta[:frame],
        theta_dot[:frame]
    )



    return (
        line1,
        line2,
        bob1,
        bob2,
        trail,
        radial_phase_point,
        radial_phase_trail,
        angular_phase_point,
        angular_phase_trail
    )

# =====================================================
# Animate
# =====================================================

frames = list(range(0, len(t_eval), 2))

ani = FuncAnimation(
    fig,
    update,
    frames=frames,
    init_func=init,
    interval=10,
    blit=True
)

# =====================================================
# Export with progress bar
# =====================================================

from tqdm import tqdm
from matplotlib.animation import FFMpegWriter

writer = FFMpegWriter(fps=60)

pbar = tqdm(total=len(frames))

ani.save(
    "oam.mp4",
    writer=writer,
    progress_callback=lambda i, n: pbar.update(1)
)

pbar.close()

plt.tight_layout()
plt.show()
