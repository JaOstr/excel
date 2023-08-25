import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.ion()

def count_down(ax):
    for i in range(10, 0, -1):
        ax.set_title(i)
        plt.pause(1)


def empty_figure():
    fig = plt.figure()
    plt.get_current_fig_manager().set_window_title("An empty figure, axes added manually")
    ax = plt.axes()
    count_down(ax)


def one_subplot():
    fig, ax = plt.subplots()
    plt.get_current_fig_manager().set_window_title("One subplot")
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
    count_down(ax)


def one_by_thress_axes():
    fig, axs = plt.subplots(1, 3)
    plt.get_current_fig_manager().set_window_title("1x3 axes")
    for i in range(axs.size):
        if i == 1:
            continue
        axs[i].set_title("Axes " + str(i))
        axs[i].plot(range((i + 1) * 3))
    count_down(axs[1])


def subplot_mosaic_ascii():
    fig, axs = plt.subplot_mosaic('''
                                AB
                                AC
                                ''')
    axs['A'].plot([1, 8, 2])
    axs['B'].plot([1, 2, 3])
    axs['C'].plot([2, 3, 4])
    count_down(axs['A'])


fig, axs = plt.subplot_mosaic([['top_left', 'top_center', 'top_right'],
                               ['bottom_left', 'bottom_right', 'bottom_right']])
x = np.linspace(-2 * np.pi, 2 * np.pi, 3000)
axs['top_left'].plot(x, np.sin(x))
axs['top_center'].plot(x, np.cos(x))
axs['top_right'].plot(x, np.sin(x) * np.cos(x))
axs['bottom_left'].plot(x, np.sin(0.5 * x))
axs['bottom_right'].plot(x, np.sin(2 * x))
count_down(axs['top_center'])


#plt.show()
