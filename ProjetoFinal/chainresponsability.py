from __future__ import annotations
from abc import ABC, abstractmethod
import random


class AtaqueHandler(ABC):
    def __init__(self):
        self._proximo=None
    
    def set_proximo(self, handler:AtaqueHandler):
        self._proximo=handler
        return handler
    
    @abstractmethod
    def handle(self,npc,alvo):
        if self._proximo:
            return self._proximo.handle(npc,alvo)
        
class FogoHandler(AtaqueHandler):
    def handle(self, npc, alvo):
        if npc.elemento == "fogo":
            dano=npc.ataque+10
            ataque="Ataque Meteoro"
            npc.atacar(alvo,dano,ataque)
            
        else:
            super().handle(npc,alvo)
            
class AguaHandler(AtaqueHandler):
    def handle(self, npc, alvo):
        if npc.elemento == "agua":
            dano=npc.ataque+10
            ataque="Ataque Tsunami"
            npc.atacar(alvo,dano,ataque)
            
        else:
            super().handle(npc,alvo)
    