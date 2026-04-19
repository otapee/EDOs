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

    def fprime(self, x, y):
        return self.q(x) - self.p(x)*y

class LinearDE2ndOrder(ABC):

    def __init__(self):
        super().__init__()
        self.__a = None
        self.__b = None
        self._r = None

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        self.__b = value

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, lambda_function):
        self._r = lambda_function

    def vprime(self, x, y, v):
        return self._r(x) - self.b*y - self.a*v

        