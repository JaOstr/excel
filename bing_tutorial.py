import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 5, 6, 7]

plt.subplot(3, 2, 1)
plt.plot(x, y)
plt.title('Line Plot')
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(3, 2, 2)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('Time')
plt.ylabel('Price')

plt.subplot(3, 2, 3)
plt.bar(x, y)
plt.title('Bar Plot')
plt.xlabel('Time')
plt.ylabel('Price')

plt.subplot(3, 2, 4)
plt.hist(y)
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('# of times')

plt.subplot(3, 2, 5)
y2 = [3, 8, 11, 2]
plt.plot(x, y, x, y2)
plt.legend(['y', 'y2'])

plt.tight_layout()

plt.show()


