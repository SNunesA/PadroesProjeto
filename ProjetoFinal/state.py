
from abc import ABC, abstractmethod


class State(ABC):
    @property
    def context(self) :
        return self._context

    @context.setter
    def context(self, context) -> None:
        self._context = context

    @abstractmethod
    def atacar(self) -> None:
        pass

    @abstractmethod
    def defender(self) -> None:
        pass


class Saudavel(State):
    def atacar(self) -> None :
        print("atacar com toda força")
        
        

    def defender(self) -> None:
        print("defender")
        
        # criar condiçao
        # self.context.transition_to(EmChamas())
    def __str__(self):
        return "Saudavel"

class EmChamas(State):
    def atacar(self) -> None:
        print("ataca mais fraco")

    def defender(self) -> None:
        print("defende mais fraco")
        
    def usarKit(self) -> None:
        print("usou kit e se curou")
        self.context.transition_to(Saudavel())
        
    def __str__(self):
        return "Em Chamas"