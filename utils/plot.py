import matplotlib.pyplot as plt
from pathlib import Path

def plot_comparision(eulers_method, analitics_y, graph_name):

    plt.clf()  # limpa o gráfico anterior

    plt.plot(eulers_method.x, eulers_method.y, label='Euler')

    plt.plot(eulers_method.x, analitics_y, '--', label='Analítica')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Euler vs Analítica')
    plt.legend()
    plt.grid(True)

    Path('output').mkdir(exist_ok=True)
    plt.savefig(Path('output') / (graph_name + '.png'))