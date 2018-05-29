import numpy as np
import matplotlib.pyplot as plt

bg_color = 'black'
fg_color = 'white'

fig = plt.figure(facecolor=bg_color, edgecolor=fg_color)
axes = fig.add_subplot(111)
axes.patch.set_facecolor(bg_color)
axes.xaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
axes.yaxis.set_tick_params(color=fg_color, labelcolor=fg_color)
for spine in axes.spines.values():
    spine.set_color(fg_color)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, 'cyan', axes=axes)
plt.xlabel('$x$', color=fg_color)
plt.ylabel('$\sin(x)$', color=fg_color)
plt.show()


# http: // sphinx-gallery.readthedocs.io/en/latest/auto_examples/sin_func/plot_sin_black_background.html
