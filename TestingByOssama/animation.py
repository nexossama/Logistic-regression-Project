import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.backends.qt_compat as qt_compat

# Set up backend
qt_compat.QApplication.setAttribute(qt_compat.Qt.AA_EnableHighDpiScaling, True)
plt.switch_backend('Qt5Agg')

# Define logistic function
def logistic(x, beta0, beta1):
    return 1 / (1 + np.exp(-(beta0 + beta1 * x)))

# Define gradient function
def gradient(x, y, beta0, beta1):
    y_hat = logistic(x, beta0, beta1)
    d_beta0 = np.mean(y_hat - y)
    d_beta1 = np.mean((y_hat - y) * x)
    return d_beta0, d_beta1

# Generate some sample data
x = np.linspace(-5, 5, 100)
y = np.random.binomial(n=1, p=logistic(x, beta0=1, beta1=2))

# Initialize plot
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
ax1, ax2 = axs
ax1.scatter(x, y)
ax1.set_xlim(-5, 5)
ax1.set_ylim(-0.1, 1.1)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Logistic Regression Fit')

# Initialize lines for fit function and gradient descent
fit_line, = ax1.plot([], [], lw=2)
grad_line, = ax2.plot([], [], lw=2)
ax2.set_xlim(0, 20)
ax2.set_ylim(-0.1, 1.1)
ax2.set_xlabel('Iteration')
ax2.set_ylabel('Parameter Value')
ax2.set_title('Gradient Descent')

# Initialize parameter values for logistic regression and gradient descent
beta0, beta1 = 0, 0
alpha = 0.05
n_iterations = 20

# Define update function for animation
def update(i):
    global beta0, beta1
    # Update logistic regression fit
    y_fit = logistic(x, beta0, beta1)
    fit_line.set_data(x, y_fit)
    # Update gradient descent
    grad_line.set_data(np.arange(i+1), [beta0] * (i+1))
    d_beta0, d_beta1 = gradient(x, y, beta0, beta1)
    beta0 -= alpha * d_beta0
    beta1 -= alpha * d_beta1
    return fit_line, grad_line,

# Create animation
anim = FuncAnimation(fig, update, frames=n_iterations, interval=500, blit=True)

# Display animation in separate window
def run_animation():
    anim._start()
    plt.show()
run_animation()
