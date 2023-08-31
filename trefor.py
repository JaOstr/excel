import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig, ax = plt.subplots()

x0 = 0
xn = 1
x = np.linspace(x0, xn)
y = x ** 2
ax.plot(x, y)


xip = 0
n = 5
for i in range(x0 * n + 1, xn * n + 1):
    xi = i / n
    yi = xi * xi
    ax.add_patch(Rectangle((xip, 0), (xn - x0) / n, yi, facecolor='none', edgecolor='blue', linewidth=0.1))
    xip = xi

plt.show()
