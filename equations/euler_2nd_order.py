from abc import ABC, abstractmethod
from equations.euler_base import EulersMethodLinearDE

class EulersMethodLinearDE2ndOrder(EulersMethodLinearDE, ABC):

    def __init__(self):
        super().__init__()


