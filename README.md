# Método de Euler para EDOs Lineares

Resolvedor numérico para equações diferenciais ordinárias lineares de primeira e talvez segunda ordem, homogêneas, não homogêneas e com coeficientes constantes usando o Método de Euler.

## Equações suportadas, até agora

y' + p(x)y = q(x)

onde p(x) e q(x) são ~~funções de potência~~ qualquer função real!!

## Instalação

```bash
git clone https://github.com/otapee/EDOs.git
cd EDOs
uv sync
```

## Uso

```python
import matplotlib.pyplot as plt
import numpy as np
from equations.euler_1st_order import EulersMethodLinearDE1stOrder

eq = EulersMethodLinearDE1stOrder()
eq.h = 0.01     # tamanho de passos. precisa ser definido antes de x
eq.x = (0, 10)      # inicio, fim
eq.p = lambda x: 3      #f unção lambda para praticidade
eq.q = lambda x: 15 * np.sin(2 * x)     # same
eq.set_y(0)     # valor de y(0)
eq.plot_func("my graph")       #nome do grafico
```

## Se quiser comparar com analítica

```python
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
plt.savefig('comparacao.png')
```

## Execute com:
```bash
uv run python main.py
```

## Dependências

- numpy
- matplotlib