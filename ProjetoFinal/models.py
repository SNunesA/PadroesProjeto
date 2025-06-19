from abc import ABC, abstractmethod
from state import (State, Saudavel, EmChamas)
# classe abstrata
class NPC(ABC):
    def __init__(self,nome,saude,ataque,defesa, elemento):
        self.nome=nome
        self.saude=saude 
        self.ataque=ataque
        self.defesa=defesa   
        self.elemento=elemento
    
    def __str__(self):
        return f"{self.nome} ({self.elemento}) - Vida: {self.saude}, Ataque: {self.ataque}, Defesa: {self.defesa}"

    def __repr__(self):
        return self.__str__()

    @abstractmethod    
    def atacar(self,alvo,dano,ataque):
        if alvo.saude>0:   
            alvo.defender() 
            if alvo.saude-dano>=0:   #se nao resultar em saude negativa           
                alvo.saude=alvo.saude-dano
                print(f"\n{self.nome} lançou {ataque} ao jogador {alvo.nome} com {dano} de dano")
            else:
                print(f"\n{self.nome} lançou {ataque} ao jogador {alvo.nome} que não resistiu ao dano")
                alvo.saude=0
    def defender(self):
        self.saude=self.saude+self.defesa

class NPCAgua(NPC):
    def __init__(self, nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa, "agua")
class NPCFogo(NPC):
    def __init__(self, nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa, "fogo")

# classes concretas
class DragonAgua(NPCAgua):
    def __init__(self, nome, saude, ataque, defesa):
       super().__init__(nome, saude, ataque, defesa)
    def atacar(self, alvo,dano,ataque):
        return super().atacar(alvo,dano,ataque)
class MageAgua(NPCAgua):
    def __init__(self,nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa)
    def atacar(self, alvo,dano,ataque):
        return super().atacar(alvo,dano,ataque)   
    

class DragonFogo(NPCFogo):
    def __init__(self,nome, saude, ataque, defesa):
       super().__init__(nome, saude, ataque, defesa)   
    def atacar(self, alvo,dano,ataque):
        return super().atacar(alvo,dano,ataque)
class MageFogo(NPCFogo):
    def __init__(self,nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa)
    def atacar(self, alvo,dano,ataque):
        return super().atacar(alvo,dano,ataque) 


# JOGADOR
class Player():
    
    _state= None
    
    def __init__(self,nome,saude,ataque,defesa):
        self.nome=nome
        self.saude=saude 
        self.ataque=ataque
        self.defesa=defesa  

        self.transition_to(Saudavel())
    #state
    def transition_to(self, state: State):

        print(f"Mudou de estado para {type(state).__name__}")
        self._state = state
        self._state.context = self

    def atacar(self,alvo):
        if alvo.saude>0:   
            alvo.defender() 
            if alvo.saude-self.ataque>=0:              
                alvo.saude=alvo.saude-self.ataque
                print(f"\n{self.nome} atacou {alvo.nome} com {self.ataque} de dano")
            else:
                print(f"\n{self.nome} atacou {alvo.nome} que não resistiu ao dano")
                alvo.saude=0
        self._state.atacar()#STATE

    def defender(self):
        self.saude=self.saude+self.defesa
        self._state.defender()#STATE

    # decorator
    def operation(self) ->str:
        return "Jogador"

    def __str__(self):
        return f"{self.nome} - Vida: {self.saude}, Ataque: {self.ataque}, Defesa: {self.defesa} , Estado:{self._state}"

    def __repr__(self):
        return self.__str__()
#  --------------------------
 
        
