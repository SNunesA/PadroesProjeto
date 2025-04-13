from factory_npc2 import create_NPC,create_Player

#python3 npc2/cliente.py 

if __name__ == "__main__":
    inimigo1 = create_NPC()
    inimigo2 = create_NPC()
    player1 = create_Player()

    while inimigo1.saude > 0 and inimigo2.saude > 0 and player1.saude > 0:
        inimigo1.atacar(player1)
        if player1.saude==0: break
        
        player1.atacar(inimigo1)
        if inimigo1.saude==0: break 
        
        inimigo2.atacar(player1)
        if player1.saude==0: break
        
        player1.atacar(inimigo2)
        
    print(f"Saude do {inimigo1.nome}:",inimigo1.saude)
    print(f"Saude do {inimigo2.nome}:",inimigo2.saude)
    print(f"Saude do {player1.nome}:",player1.saude)
