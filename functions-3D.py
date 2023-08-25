import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3)
y = np.linspace(-3, 3)
x, y = np.meshgrid(x, y)
z = np.sin(x) * np.sin(y)

ax = plt.figure().add_subplot(projection = '3d')
ax.plot_surface(x, y, z)
plt.show()
