
from abc import ABC, abstractmethod
#  Abstrai: a variação de comportamento de um objeto de acordo com seu estado interno.
# Player
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
    def defender(self,ataque) -> None:
        pass


class Saudavel(State):
    def atacar(self) -> None :
        # estado e nerf
        return "agressivamente", 0

    def defender(self,ataque) -> None:
        if ataque == "Ataque Meteoro":
            self.context.transition_to(EmChamas())
            return -2
        # nerf
        return 0
    def __str__(self):
        return "Saudavel"

class EmChamas(State):
    def atacar(self) -> None:
        # estado e nerf
        return "brandamente", -4

    def defender(self,ataque) -> None:
        # nerf
        return -2
        
    def usarKit(self,nome) -> None:
        print(f"{nome} usou Kit de Cura do inventario e ficou Saudavel")
        self.context.transition_to(Saudavel())
        
    def __str__(self):
        return "Em Chamas"