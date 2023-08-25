import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8*np.pi, 8*np.pi, 10000)
y1 = np.sin(x) / x
y2 = np.sin(x ** 2)

#plt.plot(x, y)
#plt.title()

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y1)
axs[0].set_title(r'$\frac{\sin(x)}{x}$')
axs[1].plot(x, y2)
axs[1].set_title(r'$\sin(x^2)$')
plt.show()
