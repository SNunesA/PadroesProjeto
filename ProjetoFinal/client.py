import json
from abstractfactory import (AguaFactory,FogoFactory)
from models import Player
from decoratorequip import (Espada, Kit, Armadura) 
from chainresponsability import(FogoHandler,AguaHandler)

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

    escolha=input(f"Escolha apenas um dos equipamentos:\n 1- Kit (+10 saude) \n 2-Armadura (+10 defesa)\n 3-Espada (+10 ataque)\n")
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
        
    print(player1) #arrumar o print do state
    inimigo1=lista[0]
    inimigo2=lista[1] 
        
        
    # cadeia de ataque
    fogo=FogoHandler()
    agua=AguaHandler()
    # posso inserir mais ataques depois
    fogo.set_proximo(agua)
    while inimigo1.saude > 0 and inimigo2.saude > 0 and player1.saude > 0:
                
        # inimigo1.atacar(player1, dano)
        fogo.handle(inimigo1, player1)
    
        if player1.saude==0: break
        
        player1.atacar(inimigo1)
        
        if inimigo1.saude==0: break 
                
        # inimigo2.atacar(player1, dano)
        fogo.handle(inimigo2,player1)
    
        if player1.saude==0: break
        
        player1.atacar(inimigo2)
    
            
        
