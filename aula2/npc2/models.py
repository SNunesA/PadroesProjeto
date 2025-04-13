from abc import ABC, abstractmethod

# classe abstrata
class NPC(ABC):
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
                print(f"\n{self.nome} atacou {alvo.nome}")
            else:
                alvo.saude=0
    def defender(self):
        self.saude=self.saude+self.defesa
# classes concretas
class Dragon(NPC):
    def __init__(self):
       super().__init__("Dragon", 100, 30, 5)   
    def atacar(self, alvo):
        return super().atacar(alvo)
class Mage(NPC):
    def __init__(self,):
        super().__init__("Mage", 100, 15, 15)
    def atacar(self, alvo):
        return super().atacar(alvo)   

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
                print(f"\n{self.nome} atacou {alvo.nome}")
            else:
                alvo.saude=0
    def defender(self):
        self.saude=self.saude+self.defesa
        
class Mario(Player):
    def __init__(self):
        super().__init__("Mario", 100, 12, 8)
    def atacar(self, alvo):
        return super().atacar(alvo)
    
class Joker(Player):
    def __init__(self):
        super().__init__("Joker", 120, 18, 5)
    def atacar(self, alvo):
        return super().atacar(alvo)