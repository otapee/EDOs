from abc import ABC, abstractmethod
from equations.euler_base import EulersMethodLinearDE

class EulersMethodLinearDE1stOrder(EulersMethodLinearDE, ABC):

    def __init__(self):
        super().__init__()
    
    def set_y(self, y0):
        self._y = []
        self._y.append(y0)
        i = 1
        while i < len(self.x):
            self._y.append(self.y[i-1] + self.f(self.x[i-1], self.y[i-1])*self.h)
            i+=1
