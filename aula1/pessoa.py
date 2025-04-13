#atributos nome, renda anual, cpf e cnpj
# classe abstrata
from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, renda): #construtor
        #declaraçao e inicializaçao no construtor
        self.nome=nome  #atributo
        self.renda=renda
    def mostrarnome(self):
        print("Nome:",self.nome)
    def mostrarrenda(self):
        print("Renda Anual:",self.renda)    
    @abstractmethod
    def calcularIR(self): #metodo abstrato
        pass
   

#classe concreta
class PessoaFisica(Pessoa):
    def __init__(self,nome:str, renda:float, cpf:str):
        super().__init__(nome,renda)
        self.cpf=cpf
    def calcularIR(self):
        i=self.renda*0.25
        print("Imposto PF:",i)
class PessoaJuridica(Pessoa):
    def __init__(self, nome:str, renda:float, cnpj:str):
        super().__init__(nome,renda)
        self.cpnj=cnpj
    def calcularIR(self):
        i=self.renda*0.18
        print("Imposto PJ:",i)
        
        
estudante=PessoaFisica("stefhany", 500, "4840850")
estudante.mostrarnome()
estudante.mostrarrenda()
estudante.calcularIR()

#---------------------------
ifpr=PessoaJuridica("campus foz",1000.50,"545422")
ifpr.mostrarnome()
ifpr.mostrarrenda()
ifpr.calcularIR()
