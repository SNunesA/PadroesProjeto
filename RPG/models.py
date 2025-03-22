
from abc import ABC, abstractmethod

#class Player: criar ainda

#classe pai
class NPC:
    @abstractmethod
    def __init__(self, nome, saude, forca_ataque, forca_defesa):
        self.nome = nome
        self.saude = saude
        self.forca_ataque = forca_ataque
        self.forca_defesa = forca_defesa

    def atacar(self, alvo):
        if self.saude > 0:
            dano = max(self.forca_ataque - alvo.forca_defesa, 0)
            print(f"\n{self.nome} ataca {alvo.nome} causando {dano} de dano!")
            alvo.defender(dano)
        else:
            print(f"\n{self.nome} não pode atacar, pois está fora de combate!")

    def defender(self, dano):
        self.saude = max(self.saude - dano, 0)
        print(f"{self.nome} agora tem {self.saude} de saúde.")
#classes filhas
class Dragon(NPC):
    def __init__(self):
        super().__init__("Dragon", 100, 30, 5)

class Mage(NPC):
    def __init__(self):
        super().__init__("Mage", 100, 15, 15)
