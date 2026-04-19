from abc import ABC
from graph.graph_base import GraphR2
from equations.linear_edo import LinearDE1stOrder, LinearDE2ndOrder

class BaseEulerMethod(ABC):

    def __init__(self):
        super().__init__()
        self.__h = None
    
    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        self.__h = value

class EulersMethodLinearDE1stOrder(BaseEulerMethod, GraphR2, LinearDE1stOrder):

    def __init__(self):
        super().__init__()

    def set_y(self, y0):
        self._y = [y0]
        i = 1
        while i < len(self.x):
            self._y.append(self._y[i-1] + self.fprime(self.x[i-1], self._y[i-1]) * self.h)
            i+=1

class EulersMethodLinearDE2ndOrder(BaseEulerMethod, GraphR2, LinearDE2ndOrder):

    def __init__(self):
        self.__v = None
        super().__init__()
        
    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, list):
        self.__v = list

    def set_y(self, y0, v0):
        self._y = [y0]
        self.v = [v0]
        i = 1
        while i < len(self.x):
            self._y.append(self.y[i-1] + self.v[i-1] * self.h)
            self.v.append(self.v[i-1] + (self._r(self.x[i-1]) - self.b*self.y[i-1] - self.a*self.v[i-1]) * self.h)
            i+=1



