import hashlib
from abc import ABC, abstractmethod

class PasswordStrategy(ABC):
#1 interface da estrategia
#  define o contrato, todos os outros vao ter que utilizar o encrypt
    @abstractmethod
    def encrypt(self, password:str) ->str:
        pass

# pelo padrao da strategie, todas as estrategias sao implementadas em classes
#qualquer uma dessas classes abaixo pode ser excluida sem quebrar o codigo 
class MD5Strategy(PasswordStrategy):
    def encrypt(self,password: str) -> str:
        return hashlib.md5(password.encode()).hexdigest()

class SHA1Strategy(PasswordStrategy):
    def encrypt(self,password: str) -> str:
        return hashlib.sha1(password.encode()).hexdigest()

class SHA256Strategy(PasswordStrategy):
    def encrypt(self,password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()
    

    #FACTORY DA STRATEGIES

def create(choice: int) -> PasswordStrategy:
    if type == 1: 
        return MD5Strategy()
    elif type == 2:
        return SHA1Strategy()
    elif type == 3:
        return SHA256Strategy()
    else:
        raise ValueError("invalid choice")
    