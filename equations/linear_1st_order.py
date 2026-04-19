from equations.euler_1st_order import EulersMethodLinearDE1stOrder

class LinearDE1stOrder(EulersMethodLinearDE1stOrder):

    def __init__(self):
        super().__init__()
        self.__const_list = []
        self.__power_list = []
        
    @property
    def const_list(self):
        return self.__const_list

    @const_list.setter
    def const_list(self, list):
        self.__const_list = [value for value in list]

    @property
    def power_list(self):
        return self.__power_list

    @power_list.setter
    def power_list(self, list):
        self.__power_list = [value for value in list]

    def p(self, x_i):
        return self.const_list[0]*((x_i)**self.power_list[0])

    def q(self, x_i):
        return self.const_list[1]*((x_i)**self.power_list[1])

    def f(self, x_i, y_i):
        return self.q(x_i) - self.p(x_i)*y_i