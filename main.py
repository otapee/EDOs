import matplotlib.pyplot as plt
import numpy as np
from equations.euler_1st_order import EulersMethodLinearDE1stOrder

eq = EulersMethodLinearDE1stOrder()
eq.h = 0.01
eq.x = (0, 10)
eq.p = lambda x: 3
eq.q = lambda x: 15 * np.sin(2 * x)
eq.set_y(0)
eq.plot_func("func4")

# solução analítica
x = np.arange(0, 10, 0.01)
y_analitica = ((45 * np.sin(2 * x) - 30 * np.cos(2 * x)) + 30*(np.exp(x * (-3))))/13

plt.plot(eq.x, eq.y, label='Euler')
plt.plot(x, y_analitica, '--', label='Analítica')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Euler vs Analítica')
plt.legend()
plt.grid(True)
plt.savefig('comparacao4.png')