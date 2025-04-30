from originator import Originator

class Caretaker:
    """
    O Caretaker não depende da classe concreta do Memento. Portanto,
    ele não tem acesso ao estado interno do Originator, que está armazenado
    dentro do memento. Ele trabalha com todos os mementos através da interface
    base Memento.
    """

    def __init__(self, originator: Originator) -> None:
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Salvando o estado do Originator...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not len(self._mementos):
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restaurando estado para: {memento.get_name()}")
        try:
            self._originator.restore(memento)
        except Exception:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Aqui está a lista de mementos:")
        for memento in self._mementos:
            print(memento.get_name())
