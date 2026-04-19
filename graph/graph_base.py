from abc import ABC, abstractmethod
import matplotlib.pyplot as plt
import numpy as np

class GraphR2(ABC):

    def __init__(self):
        self.__x = None
        self._y = None      # protegido, acessível nas subclasses

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, parameters):

        if self.h is not None:
            start, end, = parameters        # unpacking da tupla parameters
            self.__x = np.arange(start, end, self.h)      # n_points pontos entre start e end

    @property
    def y(self):
        return self._y
    
    @abstractmethod
    def set_y(self):        #função a definir
        pass

    def plot_func(self, graph_name):
        if self.y is not None:
            plt.plot(self.x, self.y)
            plt.xlabel('Eixo X')
            plt.ylabel('Eixo Y')
            plt.title(graph_name)
            plt.grid(True)
            plt.savefig(graph_name)