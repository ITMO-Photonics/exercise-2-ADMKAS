import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-10.,10.,500)

fig, ax = plt.subplots()

def f(x):
    return np.sqrt(np.fabs(x))*(np.sin(x**2))

y=f(x)

ax.plot(x,y)
ax.set_xlim([-7.,7.])

plt.show()
