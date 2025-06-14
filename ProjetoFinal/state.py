from models import Player
from abc import ABC, abstractmethod

class State(ABC):

    @property
    def context(self) -> Player:
        return self._context

    @context.setter
    def context(self, context: Player) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

class Saudavel(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(Envenenado())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class Envenenado(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(Saudavel())