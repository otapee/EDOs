# Método de Euler para EDOs Lineares

Resolvedor numérico para equações diferenciais ordinárias lineares de primeira e segunda ordem, homogêneas, não homogêneas e com coeficientes constantes usando o Método de Euler.

## Equações suportadas, até agora

y' + p(x)y = q(x)

onde p(x) e q(x) são funções de potência.

## Instalação

git clone https://github.com/seu-usuario/euler-project
cd euler-project
uv sync

## Uso

from equations.linear_1st_order import LinearDE1stOrder

eq = LinearDE1stOrder()
eq.x = (1, 10, 0.01)
eq.h = 0.01
eq.const_list = [2, 1]
eq.power_list = [-1, 1]
eq.set_y(1)
eq.plot_func("minha_equacao")

## Dependências

- numpy
- matplotlib