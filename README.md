Here’s a clean, professional **README.md** you can directly copy into your GitHub repo:

---

# 🧠 Computational Physics

Small, focused projects exploring how **Physics and Mathematics interact computationally**.
This repository is aimed at building intuition through simulations, visualization, and interactive models.

---

## 📌 Project 1: Logistic Map & Bifurcation Diagram

An interactive simulation of the **logistic map**, a classic example of how simple nonlinear systems can exhibit complex and chaotic behavior.

### 🔍 Features

* Interactive control of parameter ( r )
* Visualization of:

  * Time evolution of the logistic map
  * Bifurcation diagram
* Built using **Marimo** for interactivity

---

### ⚙️ Dependencies

Make sure you have the following Python packages installed:

* `marimo`
* `numpy`
* `scipy`
* `matplotlib`

You can install them using:

```bash
pip install marimo numpy scipy matplotlib
```

---

### ▶️ Run the Simulation

```bash
marimo run logistic_v2.py
```

---

### 📘 What is the Logistic Map?

The logistic map is defined as:

[
x_{n+1} = r x_n (1 - x_n)
]

* ( x ): population (normalized)
* ( r ): growth rate parameter

As ( r ) increases, the system transitions from:

* Stable equilibrium → periodic oscillations → chaos

---

### 🎯 Purpose of This Project

* Understand **nonlinear dynamics**
* Visualize **chaos and bifurcation**
* Learn how computation enhances physical intuition

---

### 🚀 Future Plans

* Add Lyapunov exponent visualization
* Explore other chaotic systems (Henon map, Lorenz system)
* Improve UI/UX with more controls

---

### 🤝 Contributions

Feel free to fork, open issues, or suggest improvements.

---


## 📌 Project 2: Oscillating Atwood Machine Simulation

A numerical simulation and animation of the **Oscillating Atwood Machine (OAM)** — a nonlinear dynamical system where one mass swings like a pendulum while connected to a counterweight through pulleys.

### 🔍 Features

* Numerical integration using `scipy.solve_ivp`
* Real-time animation with `matplotlib.animation`
* Visualization of:

  * Pendulum motion
  * Counterweight motion
  * Rope dynamics
  * Trajectory trail of the swinging mass
* MP4 export using `ffmpeg`

---

### ⚙️ Dependencies

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

#### Fedora

```bash
sudo dnf install ffmpeg
```

#### Ubuntu/Debian

```bash
sudo apt install ffmpeg
```

---

### ▶️ Run the Simulation

```bash
python oscillating_atwood.py
```

The animation will automatically save as:

```text
oscillating_atwood_machine.mp4
```

---

### 📘 What is the Oscillating Atwood Machine?

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

\ddot r = \frac{m_1 g \cos\theta - (m_1+m_2)g + m_1 r \dot\theta^2}{m_1+m_2}

and

\ddot\theta = \frac{-g\sin\theta - 2\dot r\dot\theta}{r}

---

### 🎯 Purpose of This Project

* Explore **nonlinear dynamics**
* Study coupled mechanical systems
* Visualize numerical solutions of differential equations
* Learn computational physics techniques

---

### 🚀 Future Plans

* Add energy conservation plots
* Include phase-space visualization
* Add interactive parameter controls
* Create a WebGL / Three.js version
* Explore chaotic regimes and Poincaré sections

---

### 🤝 Contributions

Feel free to fork the project, open issues, or suggest improvements.


