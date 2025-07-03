from models import Player
from state import Saudavel
class PlayerBuilder:
    
    def __init__(self, nome, saude, ataque, defesa, kits=1):
        self.nome = nome
        self.saude = saude
        self.ataque = ataque
        self.defesa = defesa
        self.kits = kits
        self.estado_inicial = Saudavel()
        
    def set_nome(self, nome):
        self.nome = nome
        return self

    def set_saude(self, saude):
        self.saude = saude
        return self

    def set_ataque(self, ataque):
        self.ataque = ataque
        return self

    def set_defesa(self, defesa):
        self.defesa = defesa
        return self
    
    def set_kits(self, kits):
        self.kits = kits
        return self

    def set_estado_inicial(self, estado):
        self.estado_inicial = estado
        return self
    
    def build(self):
        player = Player(
            nome=self.nome,
            saude=self.saude,
            ataque=self.ataque,
            defesa=self.defesa
        )
        player.kits = self.kits
        player.transition_to(self.estado_inicial)
        return player