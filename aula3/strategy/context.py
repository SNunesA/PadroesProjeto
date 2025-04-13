
""" 
Fornece um ponto de acesso para a classe cliente
delegando a execucao do calculo do hash para a estrategia
concreta
"""
import strategies 

def select_strategy() -> strategies.PasswordStrategy:
    """    Helper function - read user choice    """
    print("-"*40)
    print("Algoritmos Hash disponiveis")
    print("-"*40)
    print("""
    1 - md5
    2 - sha1
    3 - sha256
    """)
    choice = int(input("Escolha a opção: "))
    return strategies.create(choice)

class HashContext():
    #vai receber qual o tipo de hash q vai ser feito, md5 ou sha1
    def __init__(self,strategy: strategies.PasswordStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: strategies.PasswordStrategy):
        self.strategy = strategy

    def hash(self,password:str) -> str:
        "ponto de acesso ao cliente"
        if len(password) < 8:
            raise ValueError("senha não cumpriu o numero minimo de 8 caracteres")
        return self.strategy.encrypt(password) #nao sabemos qual estrategia vai ser executada
        