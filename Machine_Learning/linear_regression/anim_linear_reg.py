
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tqdm import tqdm

data = np.load("data.npz")

X = data["x"].reshape(-1)
y = data["y"].reshape(-1)

# Initial parameters
a, b = 0, 0
lr = 0.0001
N = len(X)
epochs = 1000

# Store training history
loss_history = []
training_a = []
training_b = []

# Gradient descent
for epoch in tqdm(range(epochs)):
    y_pred = a * X + b
    error = y_pred - y

    loss = np.mean(error**2)

    da = (2 / N) * np.sum(error * X)
    db = (2 / N) * np.sum(error)

    # Store parameters and loss from the same step
    training_a.append(a)
    training_b.append(b)
    loss_history.append(loss)

    # Update parameters
    a -= lr * da
    b -= lr * db

# Final estimates
estd_a = a
estd_b = b

print(f"Estimated a = {estd_a:.6f}")
print(f"Estimated b = {estd_b:.6f}")
print(f"Final MSE = {np.mean((estd_a * X + estd_b - y)**2):.6f}")

# Sort X for a correctly drawn fitted line
order = np.argsort(X)
X_sorted = X[order]

# Create figure and axes
fig = plt.figure(figsize=(16, 5))

fig.suptitle(
    "Linear Regression: Fit, Training Loss, and Parameter Landscape",
    fontsize=16,
    fontweight="bold",
    y=0.98,
)

ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133, projection="3d")

# Plot 1: Observations and changing fitted line
ax1.scatter(X, y, s=20, label="Observed data")
line, = ax1.plot([], [], "r-", lw=2, label="Fitted line")
ax1.set_xlabel("X")
ax1.set_ylabel("y")
ax1.legend()
ax1.grid(True)

# Plot 2: Loss history
loss_line, = ax2.plot([], [], "b-", lw=2)
loss_point, = ax2.plot([], [], "ro")
ax2.set_xlabel("Epoch")
ax2.set_ylabel("MSE")
ax2.set_title("Training Loss")
ax2.grid(True)

ax2.set_xlim(0, epochs - 1)
ax2.set_ylim(0, max(loss_history) * 1.1)

# Plot 3: Parameter trajectory
trajectory, = ax3.plot([], [], [], "g-", lw=2)
current_point, = ax3.plot([], [], [], "ro", markersize=6)

ax3.set_xlabel("Slope a")
ax3.set_ylabel("Intercept b")
ax3.set_zlabel("MSE")
ax3.set_title("Loss Landscape Trajectory")

# Set reasonable 3D viewing limits
pad_a = max(np.ptp(training_a) * 0.2, 0.01)
pad_b = max(np.ptp(training_b) * 0.2, 0.01)

ax3.set_xlim(min(training_a) - pad_a, max(training_a) + pad_a)
ax3.set_ylim(min(training_b) - pad_b, max(training_b) + pad_b)
ax3.set_zlim(0, max(loss_history) * 1.1)

# Animation update function
def update(frame):
    estd_a = training_a[frame]
    estd_b = training_b[frame]
    current_loss = loss_history[frame]

    # Update fitted line
    line.set_data(X_sorted, estd_a * X_sorted + estd_b)

    # Update loss curve
    loss_line.set_data(
        np.arange(frame + 1),
        loss_history[:frame + 1]
    )
    loss_point.set_data([frame], [current_loss])

    # Update 3D trajectory
    trajectory.set_data(
        training_a[:frame + 1],
        training_b[:frame + 1]
    )
    trajectory.set_3d_properties(loss_history[:frame + 1])

    current_point.set_data([estd_a], [estd_b])
    current_point.set_3d_properties([current_loss])

    # Display estimated parameters in the title
    ax1.set_title(
        f"Epoch {frame + 1}/{epochs}\n"
        f"estd_a = {estd_a:.2f}, estd_b = {estd_b:.2f}"
    )

    return (
        line, loss_line, loss_point,
        trajectory, current_point
    )

ani = FuncAnimation(
    fig,
    update,
    frames=epochs,
    interval=10,
    blit=False,
    repeat=True
)

#ani.save("linear_reg.mp4",writer='ffmpeg',fps=60)
pbar = tqdm(desc="Saving video (calculating frames...)", unit=" frames")
initialized = False


def progress_callback(curr_frame, total):
  global initialized
  if total and not initialized:
    pbar.total = total
    pbar.desc = "Saving video"
    pbar.refresh()
    initialized = True

  pbar.n = curr_frame + 1
  pbar.refresh()


try:
  ani.save(
      "linear_reg.mp4",
      writer="ffmpeg",
      fps=60,
      progress_callback=progress_callback,
  )
finally:
  pbar.close()


plt.tight_layout()
plt.show()