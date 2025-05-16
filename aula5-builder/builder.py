class Notebook:
    def __init__(self, gpu=None):
        self.gpu = None
        self.cpu=None
        self.ram=None
        self.ssd=None
        self.tela=None

    def __repr__(self):
        return f"""Notebook:{id(self)} \n 
                modelo:{self.cpu} \n 
                gpu:{self.gpu} \n 
                ram:{self.ram}"""

class NoteBuilder:
    def __init__(self):
        self.notebook=Notebook()

    def add_gpu(self):
        self.notebook.gpu="rtx"
        return self
    def add_ram(self,ram):
        self.notebook.ram=ram
        return self

    def build(self) -> Notebook:
        return self.notebook

if __name__ == "__main__":
    #usuario seleciona as opçoes
    note= (NoteBuilder()
           .add_gpu()
           .add_ram("8gb")
           .build())
    print(note) #repr

    note2=(NoteBuilder().build())
    print(note2)
