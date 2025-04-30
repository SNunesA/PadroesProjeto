from factory_npc2 import create_NPC,create_Player
from context import AtaqueContext, select_strategy 
from caretaker import Caretaker
from colorama import init, Fore, Style
init()
#python3 npc2/cliente.py 

if __name__ == "__main__":
    inimigo1 = create_NPC()
    inimigo2 = create_NPC()
    player1 = create_Player()
    print(f"NPCs: {inimigo1.nome} e {inimigo2.nome}")
    print(f"Player: {player1.nome}")

    caretaker1=Caretaker(inimigo1)
    caretaker2=Caretaker(inimigo2)
    c1=0
    c2=0
    while inimigo1.saude > 0 and inimigo2.saude > 0 and player1.saude > 0:
        #estrategia do inimigo 1
        strategy1=select_strategy()
        context=AtaqueContext(strategy1)
        dano=context.forca_ataque(inimigo1)
         
        inimigo1.atacar(player1, dano)
        if player1.saude==0: break
        caretaker1.backup()
        
        player1.atacar(inimigo1)
        
        if inimigo1.saude==0: 
            if c1==0:
                caretaker1.undo()
                print(f"{Fore.RED}Necromante reviveu {inimigo1.nome} com {inimigo1.saude} de vida{Style.RESET_ALL}")
            else:
                break
            c1=c1+1
             
        
        #estrategia do inimigo 2
        strategy2=select_strategy()
        context=AtaqueContext(strategy2)
        dano=context.forca_ataque(inimigo2)
        
        inimigo2.atacar(player1, dano)
    
        if player1.saude==0: break
        
        caretaker2.backup()
        
        player1.atacar(inimigo2)
       
        if inimigo2.saude==0: 
            if c2==0:
                caretaker2.undo()
                print(f"{Fore.RED}Necromante reviveu {inimigo2.nome} com {inimigo2.saude} de vida{Style.RESET_ALL}")
            else:
                break
            c2=c2+1
        
    print(f"Saude do {inimigo1.nome}:",inimigo1.saude)
    print(f"Saude do {inimigo2.nome}:",inimigo2.saude)
    print(f"Saude do {player1.nome}:",player1.saude)
