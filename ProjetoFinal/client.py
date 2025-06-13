import json
from abstractfactory import (AguaFactory,FogoFactory)
from models import Player
from decoratorequip import Espada 

def Create_Player(p)->Player:
    nome=input("Qual seu nome Jogador?")
    # saude=input("Quanto de vida você tem?")
    # ataque=input("Quanto a força do seu ataque?")
    # defesa=input("Qual a força da sua defesa?")
    # return Player(nome,saude,ataque,defesa)
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

    equipado=input("Deseja equipar espada?(s/n)")
    if equipado == "s":
        espada=Espada(jogador1)
        print(espada.status)
    else:
        print(jogador1)
    
    print('NPCs')
    for c in lista: 
        print(c)