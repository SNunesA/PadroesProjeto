from abc import ABC, abstractmethod
from state import (State, Saudavel, EmChamas)

# estilo
from colorama import init, Fore, Style
init()
from time import sleep

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
            if alvo.saude-dano>0:   #se nao resultar em saude negativa           
                print(f"\n{Fore.RED}{self.nome} lançou {ataque} ao jogador {alvo.nome} com {dano} de dano{Style.RESET_ALL}")
                sleep(0.5)
                nerf=alvo.defender(ataque)     
                danocomdefesa=dano-(alvo.defesa+nerf)
                alvo.saude-=danocomdefesa
            else:
                print(f"\n{Fore.RED}{self.nome} lançou {ataque} ao jogador {alvo.nome} que não resistiu ao dano{Style.RESET_ALL}")
                alvo.saude=0
    def defender(self):
        print(f'{Fore.LIGHTYELLOW_EX}{self.nome} usou sua magia de {self.defesa} pontos de defesa{Style.RESET_ALL}')

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
    
    def __init__(self,nome,saude,ataque,defesa,kits):
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
            print(f"{Fore.MAGENTA}{self.nome} sofreu um ataque de fogo e está {type(state).__name__}{Style.RESET_ALL}")
            if self.kits>0:
                self.kits-=1
                self._state.usarKit(self.nome)
            else:
                print(f"{self.nome} nao tem kits de cura")

    def atacar(self,alvo):
        if alvo.saude>0:   
            # recebe uma string e um inteiro
            estado,nerf=self._state.atacar()#STATE
            nerf+=self.ataque
            danocomdefesa=nerf-alvo.defesa
            if alvo.saude-danocomdefesa>0:              
                alvo.saude=alvo.saude-danocomdefesa
                print(f"\n{Fore.BLUE}{self.nome} atacou {estado} {alvo.nome} com {nerf} de dano{Style.RESET_ALL}")
                sleep(0.5)
                alvo.defender() 
            else:
                print(f"\n{Fore.BLUE}{self.nome} atacou {alvo.nome} que não resistiu ao dano{Style.RESET_ALL}")
                alvo.saude=0

    def defender(self, ataque):
        nerf=self._state.defender(ataque)#STATE
        print(f'{Fore.LIGHTYELLOW_EX}{self.nome} usou seu escudo de {self.defesa+nerf} pontos de defesa{Style.RESET_ALL}')
        return nerf
    
    # decorator
    def operation(self) ->str:
        return "Jogador"

    def __str__(self,equip=''):
        return f"{self.nome}  com {equip}- Vida: {self.saude}, Ataque: {self.ataque}, Defesa: {self.defesa}, Kits:{self.kits}, Estado:{self._state}"

    def __repr__(self):
        return self.__str__()
#  --------------------------
 
        
