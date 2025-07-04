from models import Player
from state import Saudavel
# Abstrai: a construção passo a passo de objetos complexos, separando sua construção de sua representação.
class PlayerBuilder:
    
    def __init__(self):
        self.nome = "Jogador padrão"
        self.saude = None
        self.ataque = None
        self.defesa = None
        self.kits = None
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
            defesa=self.defesa,
            kits=self.kits
        )
        player.transition_to(self.estado_inicial)
        return player