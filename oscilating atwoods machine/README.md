# Oscillating Atwoods Machine

A numerical simulation and animation of the **Oscillating Atwood Machine (OAM)** — a nonlinear dynamical system where one mass swings like a pendulum while connected to a counterweight through pulleys.

## 🔍 Features

* Numerical integration using `scipy.solve_ivp`
* Real-time animation with `matplotlib.animation`
* Visualization of:

  * Pendulum motion
  * Counterweight motion
  * Rope dynamics
  * Trajectory trail of the swinging mass
* MP4 export using `ffmpeg`

---

## ⚙️ Dependencies

Make sure you have the following Python packages installed:

* `numpy`
* `scipy`
* `matplotlib`
* `ffmpeg` (required for MP4 export)

You can install the Python dependencies using:

```bash
pip install numpy scipy matplotlib
```

Install FFmpeg:

### Fedora

```bash
sudo dnf install ffmpeg
```

### Ubuntu/Debian

```bash
sudo apt install ffmpeg
```

---

## ▶️ Run the Simulation

```bash
python atwood_osci.py
```

The animation will automatically save as:

```text
oscillating_atwood_machine.mp4
```

---

## 📘 What is the Oscillating Atwood Machine?

The Oscillating Atwood Machine is a modified version of the classic Atwood machine where one mass is allowed to swing freely.

The system exhibits:

* Nonlinear coupled motion
* Energy exchange between radial and angular motion
* Chaotic dynamics for certain parameters

The equations of motion are derived from **Lagrangian mechanics**.

Key generalized coordinates:

* ( r ) → pendulum length
* ( \theta ) → angular displacement

The coupled equations are:

$$\ddot r = \frac{m_1 g \cos\theta - (m_1+m_2)g + m_1 r \dot\theta^2}{m_1+m_2}$$

and

$$\ddot\theta = \frac{-g\sin\theta - 2\dot r\dot\theta}{r}$$

---

## 🎯 Purpose of This Project

* Explore **nonlinear dynamics**
* Study coupled mechanical systems
* Visualize numerical solutions of differential equations
* Learn computational physics techniques

---

## 🚀 Future Plans

* Add energy conservation plots
* Include phase-space visualization
* Add interactive parameter controls
* Create a WebGL / Three.js version
* Explore chaotic regimes and Poincaré sections
