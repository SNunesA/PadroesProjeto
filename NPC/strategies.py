from abc import ABC, abstractmethod
from random import randint
from models import Dragon, Mage
# interface da estrategia
class AtaqueStrategy(ABC):
    @abstractmethod
    def forca(self,npc)->int:
        pass
    
class AtaqueNormal(AtaqueStrategy):
    def forca(self,npc)->int:
        return npc.ataque
    
class AtaqueMaximo(AtaqueStrategy):
    def forca(self,npc)->int:
        npc.saude=npc.saude-25
        return 50
    
class AtaqueAleatorio(AtaqueStrategy):
    def forca(self,npc)->int:
        r=randint(-15,15)
        return npc.ataque+r

class AtaqueEspecifico(AtaqueStrategy):
    def forca(self,npc)->int:
        if isinstance(npc, Dragon):
            # ataque pequeno com recuperaçao de pouca saude
            npc.saude=npc.saude+10
            return npc.ataque-15
        elif isinstance(npc, Mage):
            # ataque nulo com recuperaçao de bastante saude
            npc.saude=npc.saude+25
            return 0
    
def create(choice: int) -> AtaqueStrategy:
    if choice == 1: 
        return AtaqueNormal()
    elif choice == 2:
        return AtaqueMaximo()
    elif choice == 3:
        return AtaqueAleatorio()
    elif choice == 4:
        return AtaqueEspecifico()
    else:
        raise ValueError("invalid choice")