from caretaker import Caretaker
from originator import Originator
if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Vamos retornar!\n")
    caretaker.undo()

   