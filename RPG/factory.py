from models import (
    NPC, Dragon, Mage
)
from enum import Enum #pra enumerar os tipos

class NPCType(Enum):
    Dragon = "Dragon"
    Mage = "Mage"

def create_npc(npc_type: NPCType) -> NPC:
    """ Factory method """
    if npc_type.Dragon.value == npc_type.value: 
        return Dragon() #retorna um instanciamento do tipo Dragon
    elif npc_type.Mage.value == npc_type.value: 
        return Mage() #valor padrao(default) pra qualidade
    else:
        #caso o cliente passar um tipo desconhecido ao factory
        raise ValueError("Unknown type: {npc_type}")
