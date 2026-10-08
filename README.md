# 🎯 Terminal Ballistics & Trajectory Physics Simulator

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-brightgreen.svg)](#)

A pure, zero-dependency 2D trajectory simulator and target engagement tool built from mathematical first principles in Python. It calculates kinematic flight parameters and dynamically renders a projectile arc directly in your terminal using a custom ASCII plotting engine.

---

## 🚀 Key Features

- **Mathematical First Principles:** Decomposes initial launch vectors and computes exact flight mechanics using pure trigonometry and Newtonian kinematic formulas.
- **Pure Procedural Architecture:** Built cleanly using core control flow (`while`/`for` loops, conditional branching) and Python's built-in `math` library—no heavy frameworks, NumPy, or Matplotlib required.
- **Custom Terminal ASCII Grapher:** Renders an altitude vs. distance parabolic arc within a scalable $60 \times 15$ character grid inside the command-line interface.
- **Target Engagement System:** Evaluates target tolerance margins and delivers precise error feedback (direct hit, over-shot, or under-shot).

---

## 📐 Mathematical Formulation

The simulation solves standard 2D projectile motion under constant gravitational acceleration ($g = 9.81 \, \text{m/s}^2$):

1. **Velocity Decomposition:**
   $$v_x = v_0 \cdot \cos(\theta), \quad v_y = v_0 \cdot \sin(\theta)$$

2. **Total Flight Duration:**
   $$t_{\text{flight}} = \frac{2 \cdot v_y}{g}$$

3. **Maximum Apogee (Peak Height):**
   $$H = \frac{v_y^2}{2 \cdot g}$$

4. **Total Horizontal Range:**
   $$R = v_x \cdot t_{\text{flight}}$$

5. **Analytical Parabolic Trajectory:**
   $$y(x) = x \cdot \tan(\theta) - \frac{g \cdot x^2}{2 \cdot v_x^2}$$

---

## 🛠️ Getting Started

### Prerequisites
- Python 3.8 or later installed.
- No external packages required (`pip install` is not needed).

### Installation & Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/terminal-ballistics-simulator.git
   cd terminal-ballistics-simulator