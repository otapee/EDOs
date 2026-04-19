import matplotlib.pyplot as plt
import numpy as np
from equations.linear_1st_order import LinearDE1stOrder

eq = LinearDE1stOrder()
eq.x = (0.1, 10, 0.01)
eq.h = 0.01
eq.const_list = [1, 1]
eq.power_list = [0, 1]
eq.set_y(0)
eq.plot_func("func4")

# solução analítica
x = np.arange(1, 10, 0.01)
y_analitica = x - 1 + np.exp(-x)

plt.plot(eq.x, eq.y, label='Euler')
plt.plot(x, y_analitica, '--', label='Analítica')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler vs Analítica')
plt.legend()
plt.grid(True)
plt.savefig('comparacao4.png')