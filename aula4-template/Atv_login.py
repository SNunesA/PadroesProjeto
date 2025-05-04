from abc import ABC, abstractmethod
from typing import final
class Plataforma(ABC): 
    #metodo abstrato
    @abstractmethod
    def validar_credenciais(self):#verificar plataforma
        pass
    #metodos concretos
    def logar(self,user):#salvar email do usuario
        email=user.email
        print(f"Logado com {email}")
        
    def carregar_preferencias(self):
        print("Carregando preferencias")
        
    def redirecionar(self,user):#Verifica se é funcionario ou cliente
        if isinstance(user,Funcionario):
            print("Redirecionado para Dashboard")
        elif isinstance(user,Cliente):
            print("Redirecionado para Home")
    
    #metodo template
    @final
    def Login(self): 
        user=self.validar_credenciais()
        self.logar(user)
        self.carregar_preferencias()
        self.redirecionar(user)
    

class Google(Plataforma):    
    def validar_credenciais(self):
        print("Cliente logado no Google")
        usuario1=Cliente("exemplo@cliente.com","senha")
        return usuario1

class Github(Plataforma):    
    def validar_credenciais(self):
        print("Cliente logado no GitHub")
        usuario1=Cliente("exemplo@cliente.com","senha")
        return usuario1
    
class Email(Plataforma):   
    def validar_credenciais(self):
        print("Funcionario logado no Email")
        usuario1=Funcionario("exemplo@funcionario.com","senha")
        return usuario1
        
class Usuario(ABC):
    def __init__(self,email,senha):
        self.email=email
        self.senha=senha

class Funcionario(Usuario): #email
    def __init__(self, email, senha):
        super().__init__(email, senha)

class Cliente(Usuario): #google e github
    def __init__(self, email, senha):
        super().__init__(email, senha)


if __name__ == "__main__":
    google=Google()
    google.Login()
    print('-'*40)
    github=Github()
    github.Login()
    print('-'*40)
    email=Email()
    email.Login()