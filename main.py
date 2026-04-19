import numpy as np
from equations.eulers_method import EulersMethodLinearDE1stOrder, EulersMethodLinearDE2ndOrder
from utils.plot import plot_comparision

if __name__ == "__main__":

    eq1 = EulersMethodLinearDE1stOrder()
    eq1.h = 0.01
    eq1.x = (0, 10)
    eq1.p = lambda x: 3
    eq1.q = lambda x: 15 * np.sin(2 * x)
    eq1.set_y(0)
    #eq1.plot_func("func4")

    # solução analítica
    y1_analitica = ((45 * np.sin(2 * eq1.x) - 30 * np.cos(2 * eq1.x)) + 30*(np.exp(eq1.x * (-3))))/13


    eq2 = EulersMethodLinearDE2ndOrder()
    eq2.h = 0.001
    eq2.x = (0, 10)
    eq2.a = 3
    eq2.b = 2
    eq2.r = lambda x: 0
    eq2.set_y(1, 0)

    # solucao analitica
    y2_analitica = 2 * np.exp(-eq2.x) - np.exp(-2*eq2.x)

    plot_comparision(eq1, y1_analitica, 'primeirograu')
    plot_comparision(eq2, y2_analitica, 'mola')