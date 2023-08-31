from matplotlib import pyplot as plt
import numpy as np

x = np.arange(1, 1001)
y = x**2
plt.plot(x, y, linewidth=5)
plt.axis([0, 1100, 0, 1100000])
plt.title('Kwadraty liczb', fontsize=24)
plt.xlabel('Wartości', fontsize=14)
plt.ylabel('Kwadraty wartości', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()

plt.scatter(x, y, s=20)
plt.title('Kwadraty liczb', fontsize=18)
plt.xlabel('Wartości', fontsize=14)
plt.ylabel('Kwadraty wartości', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
