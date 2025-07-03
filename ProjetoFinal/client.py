import json
from abstractfactory import (AguaFactory,FogoFactory)
from models import Player
from decoratorequip import (Espada, Kit, Armadura) 
from chainresponsability import(FogoHandler,AguaHandler, NormalHandler)

def Create_Player(p)->Player:
    nome=input("Qual seu nome Jogador?")
    return Player(nome,**p)

if __name__ == "__main__":
    json_file=open('ProjetoFinal/arquivo.json')
    dicionario=json.load(json_file)
    json_file.close()

    lista=[]
    for c in dicionario['NPCS']:
        if c['elemento'] == "agua":
            npc=AguaFactory.createNPC(c)
            lista.append(npc)
        elif c['elemento'] == "fogo":
            npc=FogoFactory.createNPC(c)
            lista.append(npc)
    
    player1=Create_Player(dicionario['Player'][0])

    escolha=input(f"Escolha apenas um dos equipamentos:\n 1- Poção da Vida (+10 saude) \n 2-Armadura (+10 defesa)\n 3-Espada (+10 ataque)\n")
    match escolha:
        case "1":
            equipado=Kit(player1)
        case "2":
            equipado=Armadura(player1)
        case "3":
            equipado=Espada(player1)
           
    print(equipado.status)
    
    print('NPCs')
    for c in lista: 
        print(c)
        
    
    inimigo1=lista[0]
    inimigo2=lista[1] 
        
        
    # cadeia de ataque
    fogo=FogoHandler()
    agua=AguaHandler()
    normal=NormalHandler()
    # posso inserir mais ataques depois
    fogo.set_proximo(agua).set_proximo(normal)
    print("Inicio da Batalha")
    while inimigo1.saude > 0 and inimigo2.saude > 0 and player1.saude > 0:
            
        fogo.handle(inimigo1, player1)
    
        if player1.saude==0: break

        player1.atacar(inimigo1)
        
        
        if inimigo1.saude==0: break 
                
        fogo.handle(inimigo2,player1)
    
        if player1.saude==0: break
        
        player1.atacar(inimigo2)
    print("Fim da Batalha")
    print(f"Saude do(a) jogador(a) {player1.nome}:",player1.saude)
    print(f"Saude do {inimigo1.nome}:",inimigo1.saude)  
    print(f"Saude do {inimigo2.nome}:",inimigo2.saude)
        
