import strategies

def select_strategy() -> strategies.FreteStrategy:
    """    Helper function - read user choice    """
    print("-"*40)
    print("Formas de Envio Disponiveis")
    print("-"*40)
    print("""
    1 - Aéreo
    2 - Express
    3 - Correios
    """)
    choice = int(input("Escolha a opção: "))
    return strategies.create(choice)

class FreteContext():
    def __init__(self,strategy: strategies.FreteStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy: strategies.FreteStrategy):
        self.strategy = strategy    
        
    def calcular(self,valor:float,peso:int) -> float:
        return self.strategy.calcular_total(valor,peso)  