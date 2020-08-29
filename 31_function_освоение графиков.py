# вызов библиотеки matplotlib
import matplotlib.pyplot as plt

# вызов библиотеки numpy
import numpy as np

# вызов библиотеки math
import math


# задание функций
x = np.linspace(-10, 10, 100)
y1 = [math. sin(i) for i in x]
y2 = [math. cos(i) for i in x]
y3 = [math. sqrt((900 - 4 * (i**2))/9) for i in x]

# построение 1-го графика
plt.subplot (2, 2, 1) # расположение графика
plt.plot (x, y1, "--", color="green")
plt.title ("график 1", fontsize=13)
plt.xlabel ("x", fontsize=15, color="red")
plt.ylabel ("y", fontsize=15, color="red")
plt.grid()

# построение 2-го графика
plt.subplot (2, 2, 2) # расположение графика
plt.plot (x, y2, ":", color="purple")
plt.title ("график 2", fontsize=13)
plt.xlabel ("x", fontsize=15, color="red")
plt.ylabel ("y", fontsize=15, color="red")
plt.grid()

# построение 3-го графика
plt.subplot (2, 2, 3) # расположение графика
plt.plot (x, y3, "-.", color="brown")
plt.title ("график 3", fontsize=13)
plt.xlabel ("x", fontsize=15, color="red")
plt.ylabel ("y", fontsize=15, color="red")
plt.grid()
plt.show () # Вывод графика на экран !!!!!
