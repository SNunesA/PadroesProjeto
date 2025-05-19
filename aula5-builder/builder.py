class Notebook:
    def __init__(self, gpu="RTX"):
        self.gpu: str = gpu # possibilita inicializar a gpu default
        self.cpu = None
        self.ram = None
        self.ssd = None
        self.tela = None
    def __repr__(self): #representaçao
        return f"""Notebook: {id(self)} \n
        modelo: {self.cpu} \n
        gpu: {self.gpu} \n
        ram: {self.ram} \n"""

class NoteBuilder:
    def __init__(self):
        self.notebook = Notebook()

    def set_gpu(self, gpu: str):
        self.notebook.gpu = gpu
        return self
    
    def set_ram(self, ram: str):
        self.notebook.ram = ram
        return self
    
    def set_cpu(self, cpu: str):
        self.notebook.cpu = cpu
        return self
    
    def build(self) -> Notebook:
        return self.notebook

if __name__ == "__main__":
    # usuario seleciona as opcoes
    notebook = (NoteBuilder()
                .set_gpu("RTX 4090")
                .set_ram("32GB")
                .set_cpu("Intel")
                .build()
                )
    print(notebook)#repr

    notebook2 = (NoteBuilder()
                .set_cpu("AMD")
                .build())
    print(notebook2)

"""
    builder = NoteBuilder()
    builder.set_gpu()
    .set_ram("32GB")
    .build()
"""
