from models import (NPC,NPCAgua, NPCFogo, MageAgua, DragonAgua,MageFogo,DragonFogo)
from abc import ABC,abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def createNPC(self) -> NPC:
        pass
#ELEMENTOS
class AguaFactory(AbstractFactory):
    def createNPC(dic) -> NPCAgua:
        params = {k: dic[k] for k in ("nome", "saude", "ataque", "defesa")}
        if dic['nome'] =='Dragon':
            return DragonAgua(**params)
        if dic['nome'] == 'Mage':
            return MageAgua(**params)
        
class FogoFactory(AbstractFactory):
    def createNPC(dic) -> NPCFogo:
        params = {k: dic[k] for k in ("nome", "saude", "ataque", "defesa")}
        if dic['nome'] =='Dragon':
            return DragonFogo(**params)
        if dic['nome'] == 'Mage':
            return MageFogo(**params)