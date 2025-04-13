from abc import ABC, abstractmethod
# interface da estrategia
class FreteStrategy(ABC):
    @abstractmethod
    def calcular_total(self,valor:float,peso:int)->float:
        pass
# classes concretas
class AereoStrategy(FreteStrategy):
    def calcular_total(self,valor:float,peso:int)->float:
        return valor+peso*25   

class ExpressStrategy(FreteStrategy):
    def calcular_total(self,valor:float,peso:int)->float:
        return valor+peso*15   

class CorreiosStrategy(FreteStrategy):
    def calcular_total(self,valor:float,peso:int)->float:
        return valor+peso*10    
    

def create(choice: int) -> FreteStrategy:
    if choice == 1: 
        return AereoStrategy()
    elif choice == 2:
        return ExpressStrategy()
    elif choice == 3:
        return CorreiosStrategy()
    else:
        raise ValueError("invalid choice")
    