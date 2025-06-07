from abc import ABC, abstractmethod

# classe abstrata
class NPC(ABC):
    def __init__(self,nome,saude,ataque,defesa, elemento):
        self.nome=nome
        self.saude=saude 
        self.ataque=ataque
        self.defesa=defesa   
        self.elemento=elemento
         
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

class NPCAgua(NPC):
    def __init__(self, nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa, "agua")
class NPCFogo(NPC):
    def __init__(self, nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa, "fogo")

# classes concretas
class DragonAgua(NPCAgua):
    def __init__(self):
       super().__init__("Dragon", 100, 30, 5)
    def atacar(self, alvo,dano):
        return super().atacar(alvo,dano)
class MageAgua(NPCAgua):
    def __init__(self,nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa)
    def atacar(self, alvo,dano):
        return super().atacar(alvo,dano)   
    

class DragonFogo(NPCFogo):
    def __init__(self,nome, saude, ataque, defesa):
       super().__init__(nome, saude, ataque, defesa)   
    def atacar(self, alvo,dano):
        return super().atacar(alvo,dano)
class MageFogo(NPCFogo):
    def __init__(self,nome, saude, ataque, defesa):
        super().__init__(nome, saude, ataque, defesa)
    def atacar(self, alvo,dano):
        return super().atacar(alvo,dano) 
