from models import Player


class EquipamentoDecorator(Player):
    _player: Player = None
    def __init__(self,player:Player):
        self._player=player

    @property
    def player(self) -> Player:
        return self._player
    @property
    def status(self):
        return str(self._player)
    
    def operation(self) -> str:
        return self._player.operation()

class Vida(EquipamentoDecorator):
    def __init__(self, player: Player):
        super().__init__(player)
        self._player.saude += 10
    def operation(self) -> str:
        print(1)
        return f"PoçãoVida_Equipado({self.player.operation()})"
    @property
    def status(self):
        # Acessando diretamente atributos do objeto decorado
        return self._player.__str__(equip='Poção de Vida')


class Ataque(EquipamentoDecorator):
    def __init__(self, player: Player):
        super().__init__(player)
        self._player.ataque+=10
    def operation(self) -> str:
        print(1)
        return f"PoçãoAtaque_Equipada({self.player.operation()})"
    @property
    def status(self):
        return self._player.__str__(equip='Poção de Ataque')

class Defesa(EquipamentoDecorator):
    def __init__(self, player: Player):
        super().__init__(player)
        self._player.defesa+=10
    def operation(self) -> str:
        print(1)
        return f"PoçãoDefesa_Equipada({self.player.operation()})"
    @property
    def status(self):
        return self._player.__str__(equip='Poção de Defesa')
