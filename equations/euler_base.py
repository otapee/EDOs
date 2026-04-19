from abc import ABC, abstractmethod
from graph.graph_base import GraphR2

class EulersMethodLinearDE(GraphR2, ABC):
    
    def __init__(self):
        super().__init__()
        self.__h = None

    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        self.__h = value

    @abstractmethod
    def f(self):
        pass

    @abstractmethod
    def set_y(self, y0):
        pass