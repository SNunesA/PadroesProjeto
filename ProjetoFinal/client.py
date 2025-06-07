import json
import os
from models import (NPC,NPCAgua, NPCFogo, MageAgua, DragonAgua,MageFogo,DragonFogo)
from abc import ABC,abstractmethod
class AbstractFactory(ABC):
    def createDragon(self)-> NPC:
        pass
    def createMage(self)-> NPC:
        pass
#ELEMENTOS
class aguaFactory(AbstractFactory):
    def createDragon() -> NPCAgua:
        return DragonAgua()
    def createMage() -> NPCAgua:
        return MageAgua()
    def createNPCAgua(tipo):
        if tipo =='Dragon':
            return aguaFactory.createDragon()
        # if tipo == 'Mage':



json_file=open('ProjetoFinal/arquivo.json', mode="r")
sistema=json.load(json_file)
json_file.close()


for c in sistema["NPCS"]:
    if c['elemento'] == "agua":
        npc1=aguaFactory.createNPCAgua(c['nome'])
    
print(npc1.nome)
print(npc1.elemento)

        
    