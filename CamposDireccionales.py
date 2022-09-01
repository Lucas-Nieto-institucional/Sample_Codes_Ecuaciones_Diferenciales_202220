# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 16:20:37 2022

DIFFERENTIAL EQUATION DIRECTIONAL FIELD PLOTTER

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Create location grid for arrows

x_step = 0.45
y_step = 0.45

x = np.arange(-4,4.5,x_step)
y = np.arange(-3,3.5,y_step)

X,Y = np.meshgrid(x,y)

# Input ED

def Diff_Eq(x,y):
    dydt = np.sin(x*y)/np.sqrt(1+(x**2)+(y**2))
    return dydt

dy = Diff_Eq(X,Y)
dx = np.ones(dy.shape)

# Plot 

plt.quiver(X,Y,dx,dy,color = 'k')
plt.grid()
plt.axvline(0,c='k', linestyle = '-')
plt.axhline(0,c='k', linestyle = '-')
plt.title(r'Campo direccional de $\frac{dy}{dx} =\frac{sin(xy)}{1+x^2 + y^2}$')

# Solution curves

y0 = 0  # Initial conditions
y1 = 1
y2 = -1
y3 = 2
y4 = -2

solution_1 = odeint(Diff_Eq,y0,x)
solution_2 = odeint(Diff_Eq,y1,x)
solution_3 = odeint(Diff_Eq,y2,x)
solution_4 = odeint(Diff_Eq,y3,x)
solution_5 = odeint(Diff_Eq,y4,x)

plt.plot(x,solution_4, c='purple', label = r'y(0)=2')
plt.plot(x,solution_2, c='g', label = r'y(0)=1')
plt.plot(x,solution_1, c='r', label = r'y(0)=0')
plt.plot(x,solution_3, c='b', label = r'y(0)=-1')
plt.plot(x,solution_5, c='orange', label = r'y(0)=-2')
plt.legend()
plt.show()

# Repeat for a larger data array

x_step = 2
y_step = 2

x = np.arange(-40,45,x_step)
y = np.arange(-30,35,y_step)

X,Y = np.meshgrid(x,y)

dy = Diff_Eq(X,Y)
dx = np.ones(dy.shape)

plt.quiver(X,Y,dx,dy,color = 'k')
plt.grid()
plt.axvline(0,c='k', linestyle = '-')
plt.axhline(0,c='k', linestyle = '-')
plt.title(r'Campo direccional de $\frac{dy}{dx} =\frac{sin(xy)}{1+x^2 + y^2}$')

y0 = 0
y1 = 15
y2 = -15
y3 = 30
y4 = -30

solution_1 = odeint(Diff_Eq,y0,x)
solution_2 = odeint(Diff_Eq,y1,x)
solution_3 = odeint(Diff_Eq,y2,x)
solution_4 = odeint(Diff_Eq,y3,x)
solution_5 = odeint(Diff_Eq,y4,x)

plt.plot(x,solution_4, c='purple', label = r'y(0)=30')
plt.plot(x,solution_2, c='g', label = r'y(0)=15')
plt.plot(x,solution_1, c='r', label = r'y(0)=0')
plt.plot(x,solution_3, c='b', label = r'y(0)=-15')
plt.plot(x,solution_5, c='orange', label = r'y(0)=-30')
plt.legend()
plt.show()