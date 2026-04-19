from abc import ABC

class LinearDE1stOrder(ABC):

    def __init__(self):
        super().__init__()
        self.__p = None
        self.__q = None
        
    @property
    def p(self):
        return self.__p

    @p.setter
    def p(self, lambda_function):
        self.__p = lambda_function

    @property
    def q(self):
        return self.__q

    @q.setter
    def q(self, lambda_function):
        self.__q = lambda_function

    def f(self, x, y):
        return self.q(x) - self.p(x)*y