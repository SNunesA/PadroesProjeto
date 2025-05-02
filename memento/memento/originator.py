from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from random import sample
from string import ascii_letters

class Originator:
    """
    O Originator mantém um estado importante que pode mudar ao longo do tempo.
    Ele também define um método para salvar o estado dentro de um memento e
    outro método para restaurar o estado a partir dele.
    """

    _state = None
    """
    Para simplificar, o estado do Originator é armazenado em uma única variável.
    """

    def __init__(self, state: str) -> None:
        self._state = state
        print(f"Originator: Meu estado inicial é: {self._state}")

    def do_something(self) -> None:
        """
        A lógica de negócios do Originator pode afetar seu estado interno.
        Portanto, o cliente deve fazer um backup do estado antes de executar
        métodos da lógica de negócios, usando o método save().
        """

        print("Originator: Estou fazendo algo importante.")
        self._state = self._generate_random_string(30)
        print(f"Originator: e meu estado mudou para: {self._state}")

    @staticmethod
    def _generate_random_string(length: int = 10) -> str:
        return "".join(sample(ascii_letters, length))

    def save(self) -> Memento:
        """
        Salva o estado atual dentro de um memento.
        """

        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        """
        Restaura o estado do Originator a partir de um objeto memento.
        """

        self._state = memento.get_state()
        print(f"Originator: Meu estado foi alterado para: {self._state}")


class Memento(ABC):
    """
    A interface Memento fornece uma maneira de recuperar os metadados do memento,
    como data de criação ou nome. Porém, não expõe o estado do Originator.
    """

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> str:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str) -> None:
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self) -> str:
        """
        O Originator usa este método ao restaurar seu estado.
        """
        return self._state

    def get_name(self) -> str:
        """
        Os métodos a seguir são usados pelo Caretaker para exibir metadados.
        """

        return f"{self._date} / ({self._state[0:9]}...)"

    def get_date(self) -> str:
        return self._date
