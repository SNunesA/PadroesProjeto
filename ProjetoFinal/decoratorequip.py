from models import Player


class EquipamentoDecorator(Player):
    _player: Player = None
    def __init__(self,player:Player):
        self._player=player

    @property
    def player(self) -> Player:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._player
    @property
    def status(self):
        return str(self._player)
    
    def operation(self) -> str:
        return self._player.operation()
    
class Espada(EquipamentoDecorator):
    def operation(self) -> str:
        print(1)
        return f"Espada_Equipada({self.player.operation()})"
    @property
    def status(self):
        # Acessando diretamente atributos do objeto decorado
        self._player.ataque+=10
        return f"{self._player.nome} com Espada - Vida: {self._player.saude}, Ataque: {self._player.ataque}, Defesa: {self._player.defesa}"

        