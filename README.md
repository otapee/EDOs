# Método de Euler para EDOs Lineares

Resolvedor numérico para equações diferenciais ordinárias lineares de primeira e segunda ordem, homogêneas, não homogêneas e com coeficientes constantes usando o Método de Euler.

## Equações suportadas, até agora

y'(x) + p(x)y(x) = q(x)

Onde p(x) e q(x) são ~~funções de potência~~ qualquer função real!!

y''(x) + ay'(x) + by(x) = r(x)

Onde a e b são coeficientes constantes e r(x) é qualquer função real. Pode ser 0, no caso homogêneo

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
from equations.eulers_method import EulersMethodLinearDE1stOrder, EulersMethodLinearDE2ndOrder

if __name__ == "__main__":

    eq1 = EulersMethodLinearDE1stOrder()
    eq1.h = 0.01     # tamanho de passos. precisa ser definido antes de x
    eq1.x = (0, 10)      # inicio, fim
    eq1.p = lambda x: 3      # função lambda para praticidade
    eq1.q = lambda x: 15 * np.sin(2 * x)     # same
    eq1.set_y(0)     # valor de y(0)
    eq1.plot_func("linear ordem 1")       #nome do grafico

    eq2 = EulersMethodLinearDE2ndOrder()
    eq2.h = 0.001
    eq2.x = (0, 10)
    eq2.a = 3
    eq2.b = 2
    eq2.r = lambda x: 0
    eq2.set_y(1, 0)
    eq2.plot_func("linear ordem 2 homo")
```

## Se quiser comparar com analítica

```python
from utils.plot import plot_comparision

# solução analítica, varia para cada EDO
y1_analitica = ((45 * np.sin(2 * eq1.x) - 30 * np.cos(2 * eq1.x)) + 30*(np.exp(eq1.x * (-3))))/13

plot_comparision(eq1, y1_analitica, 'primeirograu', 'Tempo[s]', 'Corrente[A]')
```

## Execute com:
```bash
uv run python main.py
```

## Dependências

- numpy
- matplotlib