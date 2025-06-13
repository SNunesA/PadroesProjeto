import json
from abstractfactory import *
from models import Player

def Create_Player()->Player:
    nome=input("Qual seu nome Jogador?")
    saude=input("Quanto de vida você tem?")
    ataque=input("Quanto a força do seu ataque?")
    defesa=input("Qual a força da sua defesa?")
    return Player(nome,saude,ataque,defesa)

if __name__ == "__main__":
    json_file=open('ProjetoFinal/arquivo.json')
    dicionario=json.load(json_file)
    json_file.close()

    lista=[]
    for c in dicionario['NPCS']:
        if c['elemento'] == "agua":
            npc=aguaFactory.createNPC(c)
            lista.append(npc)
        elif c['elemento'] == "fogo":
            npc=fogoFactory.createNPC(c)
            lista.append(npc)
        
    jogador1=Create_Player()
    print(jogador1)
    print('NPCs')
    for c in lista: 
        print(c)
            