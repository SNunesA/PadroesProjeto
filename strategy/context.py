
""" 
Fornece um ponto de acesso para a classe cliente
delegando a execucao do calculo do hash para a estrategia
concreta
"""
from strategies import PasswordStrategy
class HashContext():
    #vai receber qual o tipo de hash q vai ser feito, md5 ou sha1
    def __init__(self,strategy: PasswordStrategy):
        self.strategy = strategy

    def hash(self,password:str) -> str:
        "ponto de acesso ao cliente"
        return self.strategy.encrypt(password) #nao sabemos qual estrategia vai ser executada
        