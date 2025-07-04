from __future__ import annotations
from abc import ABC, abstractmethod
import random

# Abstrai: o envio de uma solicitação por uma cadeia de objetos, onde cada um pode processá-la ou passá-la adiante.
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
        if npc.elemento == "fogo" and random.randint(1,3)==1:
            # vai lançar um nerf no player
            dano=npc.ataque
            ataque="Ataque Meteoro"
            npc.atacar(alvo,dano,ataque)
            
        else:
            super().handle(npc,alvo)
            
class AguaHandler(AtaqueHandler):
    def handle(self, npc, alvo):
        if npc.elemento == "agua" and random.randint(1,3)==1:
            # +10 de dano
            dano=npc.ataque+10
            ataque="Ataque Tsunami"
            npc.atacar(alvo,dano,ataque)
            
        else:
            super().handle(npc,alvo)
    
class NormalHandler(AtaqueHandler):
    def handle(self, npc, alvo):
        dano=npc.ataque
        ataque="Ataque Normal"
        npc.atacar(alvo,dano,ataque)
            

            