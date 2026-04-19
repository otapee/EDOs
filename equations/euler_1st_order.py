from graph.graph_base import GraphR2
from equations.linear_1st_order import LinearDE1stOrder

class EulersMethodLinearDE1stOrder(GraphR2, LinearDE1stOrder):

    def __init__(self):
        super().__init__()
        self.__h = None
    
    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, value):
        self.__h = value
    
    def set_y(self, y0):
        self._y = []
        self._y.append(y0)
        i = 1
        while i < len(self.x):

            self._y.append(self._y[i-1] + self.f(self.x[i-1], self._y[i-1])*self.h)
            i+=1
