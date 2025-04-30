import strategies
from random import randint
def select_strategy() -> strategies.AtaqueStrategy:
 
    # 1 - Normal
    # 2 - Máximo
    # 3 - Aleatório
    # 4 - Especifico
    
    
    choice = randint(1,4)
    return strategies.create(choice)

class AtaqueContext():
    def __init__(self,strategy: strategies.AtaqueStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy: strategies.AtaqueStrategy):
        self.strategy = strategy    
        
    def forca_ataque(self,npc) -> int:
        return self.strategy.forca(npc)  