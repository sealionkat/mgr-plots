import matplotlib.pyplot as plt
import sys

print(sys.argv)


def plot_line(x, y):
  plt.plot(x, y)
  plt.show()

plot_line([1, 2, 3], [1, 4, 5])
