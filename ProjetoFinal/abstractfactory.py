from models import (NPC,NPCAgua, NPCFogo, MageAgua, DragonAgua,MageFogo,DragonFogo)
from abc import ABC,abstractmethod
# Abstrai: a criação de famílias de objetos relacionados sem especificar suas classes concretas.
class AbstractFactory(ABC):
    @abstractmethod
    def createNPC(self) -> NPC:
        pass
#ELEMENTOS
class AguaFactory(AbstractFactory):
    def createNPC(self,dic) -> NPC:
        params = {k: dic[k] for k in ("nome", "saude", "ataque", "defesa")}
        if dic['nome'] =='Dragon':
            return DragonAgua(**params)
        if dic['nome'] == 'Mage':
            return MageAgua(**params)
        
class FogoFactory(AbstractFactory):
    def createNPC(self,dic) -> NPC:
        params = {k: dic[k] for k in ("nome", "saude", "ataque", "defesa")}
        if dic['nome'] =='Dragon':
            return DragonFogo(**params)
        if dic['nome'] == 'Mage':
            return MageFogo(**params)