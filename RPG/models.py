import time

class NPC:
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

class Dragon(NPC):
    def __init__(self):
        super().__init__("Dragon", 100, 30, 5)

class Mage(NPC):
    def __init__(self):
        super().__init__("Mage", 100, 15, 15)

# Criando os personagens
dragon = Dragon()
mage = Mage()

# Loop da batalha até que um deles morra
while dragon.saude > 0 and mage.saude > 0:
    dragon.atacar(mage)  # Dragon ataca Mage
    if mage.saude == 0:
        print(f"\n{mage.nome} morreu! {dragon.nome} venceu!")
        break  # Sai do loop se o Mage morrer
    
    time.sleep(1)  # Pequena pausa para simular batalha

    mage.atacar(dragon)  # Mage ataca Dragon
    if dragon.saude == 0:
        print(f"\n{dragon.nome} morreu! {mage.nome} venceu!")
        break  # Sai do loop se o Dragon morrer
    
    time.sleep(1)  # Pequena pausa entre os turnos

# Exibindo a saúde final
print(f"\n--- Saúde Final ---")
print(f"{dragon.nome}: {dragon.saude}")
print(f"{mage.nome}: {mage.saude}")