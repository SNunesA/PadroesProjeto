from abc import ABC, abstractmethod
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
            
class Dragon(NPC):
    def __init__(self,nome):
       super().__init__(nome, 100, 30, 5)   
    def atacar(self, alvo):
        return super().atacar(alvo)
class Mage(NPC):
    def __init__(self,nome):
        super().__init__(nome, 100, 15, 15)
    def atacar(self, alvo):
        return super().atacar(alvo)    
    
vermithor=Dragon("vermithor")
strange= Mage("strange")
while vermithor.saude>0 and strange.saude>0:
    vermithor.atacar(strange)
    strange.atacar(vermithor)
    
print("Saude do dragao:",vermithor.saude)
print("Saude do mago:",strange.saude)
