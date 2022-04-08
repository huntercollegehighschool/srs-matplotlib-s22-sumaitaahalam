"""
The code below generates a certain line plot.
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 10)
#x = np.arange(0, 3, .1)

plt.plot(x, x**2, '^g', label='quadratic')
# add new plot here
# add new plot here
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Line Plots")
plt.legend()
plt.show()

"""
1. Add two more plots to the same graph using plt.plot(). One should be a linear graph (y=x), and the other should be a cubic graph (y=x^3). You can adjust the labels as necessary.
"""

"""
2. x is a set of number numbers determined by the linspace function from numpy. Adjust the third argument in the linspace function to 100. What does that control?

"""

"""
3. The x-values can also be set using numpy's arange function. Uncomment line 8, and change the .1 to .05. What is the difference between linspace and arange?

"""

"""
4. In the plt.plot() function, there's a third argument that determines the shape and color of the plots. For example, '^g' creates green triangles. You can explore more shapes and colors here:
https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.pyplot.plot.html

Use different symbols for each of your plots.
"""
