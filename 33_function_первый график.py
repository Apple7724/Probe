import matplotlib.pyplot as plt
import numpy as np
import math
# Независимая (x) и зависимая (y) переменные
x = np.linspace(-10, 10, 100)
# линейная зависимость
y1 = x
# квадратичная зависимость
y2 = [i**2 for i in x]
# sin
y3 = [20*math.sin (j) for j in x]

# Построение графика
plt.title("Зависимости: y1 = x, y2 = x^2, y3 = sin(x)") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y1, y2, y3") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y1, x, y2, x, y3)# построение графика
plt.show()
