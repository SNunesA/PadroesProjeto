from factory_npc2 import create_NPC,create_Player
from context import AtaqueContext, select_strategy 

#python3 npc2/cliente.py 

if __name__ == "__main__":
    inimigo1 = create_NPC()
    inimigo2 = create_NPC()
    player1 = create_Player()
    print(f"NPCs: {inimigo1.nome} e {inimigo2.nome}")
    print(f"Player: {player1.nome}")

    while inimigo1.saude > 0 and inimigo2.saude > 0 and player1.saude > 0:
        #estrategia do inimigo 1
        strategy1=select_strategy()
        context=AtaqueContext(strategy1)
        dano=context.forca_ataque(inimigo1)
         
        inimigo1.atacar(player1, dano)
       
        if player1.saude==0: break
        
        player1.atacar(inimigo1)
        
        if inimigo1.saude==0: break 
        
        #estrategia do inimigo 2
        strategy2=select_strategy()
        context=AtaqueContext(strategy2)
        dano=context.forca_ataque(inimigo2)
        
        inimigo2.atacar(player1, dano)
    
        if player1.saude==0: break
        
        player1.atacar(inimigo2)
       
        
    print(f"Saude do {inimigo1.nome}:",inimigo1.saude)
    print(f"Saude do {inimigo2.nome}:",inimigo2.saude)
    print(f"Saude do {player1.nome}:",player1.saude)
