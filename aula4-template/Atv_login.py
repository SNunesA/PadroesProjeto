from abc import ABC, abstractmethod
from typing import final

class Usuario(ABC):
    #metodo abstrato
    def validar_credenciais():
    
    #metodos concretos
    def logar():
        print("usuario logado")
    def carregar_preferencias():
        
    def redirecionar():
    
    #metodo template
    @final
    def Login(self): 
       
        self.validar_credenciais()
        self.logar()
        self.carregar_preferencias()
        self.redirecionar()


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

if __name__ == "__main__":