#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lotka_volterra(t, y, a, b, c, d, e, f):
    x, y, z = y
    dxdt = a*x - b*x*y - c*x*z
    dydt = d*x*y - e*y + f*y*z
    dzdt = -f*z + c*x*z - e*y*z
    return [dxdt, dydt, dzdt]

# Set parameters
a = 2
b = 1
c = 0.5
d = 1
e = 1
f = 1.5

# Set initial conditions
x0 = 5
y0 = 3
z0 = 2

# Set time range for simulation
t_start = 0
t_end = 20
t_eval = np.linspace(t_start, t_end, 1000)

# Solve the ODE system
sol = solve_ivp(lotka_volterra, [t_start, t_end], [x0, y0, z0], args=(a, b, c, d, e, f), t_eval=t_eval)

# Plot the results
plt.plot(sol.t, sol.y[0], label='Species 1 (x)')
plt.plot(sol.t, sol.y[1], label='Species 2 (y)')
plt.plot(sol.t, sol.y[2], label='Species 3 (z)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model with 3 Species')
plt.legend()
plt.show()


# In[3]:


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lotka_volterra(t, y, a, b, c, d):
    x, y = y
    dxdt = a*x - b*x*y
    dydt = c*x*y - d*y
    return [dxdt, dydt]

# Set parameters
a = 1.5
b = 0.1
c = 0.1
d = 1

# Set initial conditions
x0 = 10
y0 = 5

# Set time range for simulation
t_start = 0
t_end = 30
t_eval = np.linspace(t_start, t_end, 1000)

# Solve the ODE system
sol = solve_ivp(lotka_volterra, [t_start, t_end], [x0, y0], args=(a, b, c, d), t_eval=t_eval)

# Plot the results
plt.plot(sol.t, sol.y[0], label='Prey (x)')
plt.plot(sol.t, sol.y[1], label='Predator (y)')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Lotka-Volterra Model with 2 Species')
plt.legend()
plt.show()


# In[ ]:




