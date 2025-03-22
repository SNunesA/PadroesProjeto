import time
from factory import create_npc, NPCType, create_player, PlayerType
#executar
#python3 RPG/client.py 

# Criando os personagens
dragon = create_npc(NPCType.Dragon)
mage=create_npc(NPCType.Mage)

mario = create_player(PlayerType.Mario)
joker = create_player(PlayerType.Joker)

#mage = Mage()
#dragon = Dragon()

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