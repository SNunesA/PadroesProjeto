import json
from abstractfactory import (AguaFactory,FogoFactory)
from models import Player
from decoratorequip import (Espada, Kit, Armadura) 

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
    
    jogador1=Create_Player(dicionario['Player'][0])

    escolha=input(f"Escolha apenas um dos equipamentos:\n 1- Kit (+10 saude) \n 2-Armadura (+10 defesa)\n 3-Espada (+10 ataque)\n")
    match escolha:
        case "1":
            equipado=Kit(jogador1)
        case "2":
            equipado=Armadura(jogador1)
        case "3":
            equipado=Espada(jogador1)
           
    print(equipado.status)
    
    print('NPCs')
    for c in lista: 
        print(c)
        
    print(jogador1)