
from abc import ABC, abstractmethod
from typing import final

class Pagamento(ABC):
    def create_transaction(self):
        return 1001
    @abstractmethod #metodo que deve ser implementado
    def pagar(self):
        pass

    def gerar_nota(self):
        print(f"nota fiscal gerada para transacao")


    @final #nao pode ser sobrescrito
    def realizar_pagamento(self):
        #Metodo template
        #1.id transaçao <-concreto
        id=self.create_transaction()
        print(f"1.transacao {id} gerada")
        
        #2.pagar <- abstrato
        self.pagar()

        #3.gerar nota fiscal
        self.gerar_nota()
        print("="*40)

class Pix(Pagamento):
    def pagar(self):
        print("Pagamento pix")

class Cartao(Pagamento):
    def pagar(self):
        print("Pagamento cartao")

#cliente
if __name__=="__main__":
    pgt=Pix()
    pgt.realizar_pagamento()

    pgt=Cartao()
    pgt.realizar_pagamento()