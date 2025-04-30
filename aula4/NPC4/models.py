from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
# classe abstrata
class NPC(ABC):
    def __init__(self,nome,saude,ataque,defesa):
        self.nome=nome
        self.saude=saude 
        self.ataque=ataque
        self.defesa=defesa   
        

    def save(self)-> Memento:
        # Salva os atributos que representam o estado
        state = {
            "nome": self.nome,
            "saude": self.saude,
            "ataque": self.ataque,
            "defesa": self.defesa,
        }
        return ConcreteMemento(state)
    def restore(self, memento: Memento)-> None:
        state = memento.get_state()
        self.nome = state["nome"]
        self.saude = state["saude"]+1
        self.ataque = state["ataque"]
        self.defesa = state["defesa"]
    
    @abstractmethod    
    def atacar(self,alvo,dano):
        if alvo.saude>0:   
            alvo.defender() 
            if alvo.saude-dano>=0:   #se nao resultar em saude negativa           
                alvo.saude=alvo.saude-dano
                print(f"\n{self.nome} atacou {alvo.nome} com {dano} de dano")
            else:
                print(f"\n{self.nome} atacou {alvo.nome} que não resistiu ao dano")
                alvo.saude=0
    def defender(self):
        self.saude=self.saude+self.defesa
# classes concretas
class Dragon(NPC):
    def __init__(self):
       super().__init__("Dragon", 100, 30, 5)   
    def atacar(self, alvo,dano):
        return super().atacar(alvo,dano)
class Mage(NPC):
    def __init__(self,):
        super().__init__("Mage", 100, 15, 15)
    def atacar(self, alvo,dano):
        return super().atacar(alvo,dano)   
# memento npc
class Memento(ABC):
    """
    A interface Memento fornece uma maneira de recuperar os metadados do memento,
    como data de criação ou nome. Porém, não expõe o estado do Originator.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        O Originator usa este método ao restaurar seu estado.
        """
        return self._state

    def get_name(self) -> str:
        """
        Os métodos a seguir são usados pelo Caretaker para exibir metadados.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date



# -----------
# classe pai
class Player(ABC):
    def __init__(self,nome,saude,ataque,defesa):
        self.nome=nome
        self.saude=saude 
        self.ataque=ataque
        self.defesa=defesa   
         
    @abstractmethod    
    def atacar(self,alvo):
        if alvo.saude>0:   
            alvo.defender() 
            if alvo.saude-self.ataque>=0:              
                alvo.saude=alvo.saude-self.ataque
                print(f"\n{self.nome} atacou {alvo.nome} com {self.ataque} de dano")
            else:
                print(f"\n{self.nome} atacou {alvo.nome} que não resistiu ao dano")
                alvo.saude=0
    def defender(self):
        self.saude=self.saude+self.defesa
        
class Mario(Player):
    def __init__(self):
        super().__init__("Mario", 400, 12, 8) #saude aumentada
    def atacar(self, alvo):
        return super().atacar(alvo)
    
class Joker(Player):
    def __init__(self):
        super().__init__("Joker", 400, 18, 5) #saude aumentada
    def atacar(self, alvo):
        return super().atacar(alvo)