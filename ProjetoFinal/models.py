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
            if alvo.saude-dano>=0:   #se nao resultar em saude negativa           
                print(f"\n{self.nome} lançou {ataque} ao jogador {alvo.nome} com {dano} de dano")
                nerf=alvo.defender(ataque)     
                danocomdefesa=dano-(alvo.defesa+nerf)
                alvo.saude-=danocomdefesa
            else:
                print(f"\n{self.nome} lançou {ataque} ao jogador {alvo.nome} que não resistiu ao dano")
                alvo.saude=0
    def defender(self):
        print(f'{self.nome} usou sua magia de {self.defesa} pontos de defesa')

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
class Player:
    
    def __init__(self,nome,saude,ataque,defesa,kits=0):
        self.nome=nome
        self.saude=saude 
        self.ataque=ataque
        self.defesa=defesa  
        self.kits=kits
        # iniciando no estado saudavel
        self._state = None        
    #state
    def transition_to(self, state: State):
        self._state = state
        self._state.context = self
        if isinstance(state, EmChamas):
            print(f"{self.nome} sofreu um ataque de fogo e está {type(state).__name__}")
            if self.kits>0:
                self.kits-=1
                self._state.usarKit(self.nome)
            else:
                print(f"{self.nome} nao tem mais kits de cura")

    def atacar(self,alvo):
        if alvo.saude>0:   
            # recebe uma string e um inteiro
            estado,nerf=self._state.atacar()#STATE
            nerf+=self.ataque
            danocomdefesa=nerf-alvo.defesa
            if alvo.saude-danocomdefesa>=0:              
                alvo.saude=alvo.saude-danocomdefesa
                print(f"\n{self.nome} atacou {estado} {alvo.nome} com {nerf} de dano")
                alvo.defender() 
            else:
                print(f"\n{self.nome} atacou {alvo.nome} que não resistiu ao dano")
                alvo.saude=0

    def defender(self, ataque):
        nerf=self._state.defender(ataque)#STATE
        print(f'{self.nome} usou seu escudo de {self.defesa+nerf} pontos de defesa')
        return nerf
    
    # decorator
    def operation(self) ->str:
        return "Jogador"

    def __str__(self,equip=''):
        return f"{self.nome}  com {equip}- Vida: {self.saude}, Ataque: {self.ataque}, Defesa: {self.defesa} , Estado:{self._state}"

    def __repr__(self):
        return self.__str__()
#  --------------------------
 
        
