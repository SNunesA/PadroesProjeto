from abc import ABC, abstractmethod
from typing import final

class Usuario(ABC):
    def validar_credenciais():
        
    #metodos concretos
    def logar():

    def carregar_preferencias():

    def redirecionar():
    
    #metodo template
    def Login(self): 
        #metodo abstrato
        self.validar_credenciais()

class Funcionario(Usuario): #email

class Cliente(Usuario): #google e github

class Plataforma(ABC): 
    @abstractmethod
    def __init__(self,email):
        self.email=email

class Google(Plataforma):
    def __init__(self, email:str):
        super().__init__(email)
class Github(Plataforma):
    def __init__(self, email:str):
        super().__init__(email)

class Email(Plataforma):
    def __init__(self, email:str):
        super().__init__(email)
