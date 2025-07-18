import json
from abstractfactory import (AguaFactory,FogoFactory)
from builder import PlayerBuilder
from decoratorequip import (Vida,Defesa,Ataque) 
from chainresponsability import(FogoHandler,AguaHandler, NormalHandler)
import random
# estilo
from colorama import init, Fore, Style
init()

def criar_jogador(nome,dados):
    return (PlayerBuilder()
    .set_nome(nome)
    .set_saude(dados["saude"])
    .set_ataque(dados["ataque"])
    .set_defesa(dados["defesa"])
    .set_kits(dados["kits"])
    .build())

if __name__ == "__main__":
    json_file=open('ProjetoFinal/arquivo.json')
    dicionario=json.load(json_file)
    json_file.close()

    lista=[]
    agua_factory = AguaFactory()
    fogo_factory = FogoFactory()
    for c in dicionario['NPCS']:
        if c['elemento'] == "agua":
            npc = agua_factory.createNPC(c)
            lista.append(npc)
        elif c['elemento'] == "fogo":
            npc=fogo_factory.createNPC(c)
            lista.append(npc)


    nome=input("Qual seu nome Jogador?\n")
    classe=input("Qual classe você deseja? (Guerreiro | Arqueiro)\n")
    for c in dicionario['Player']:
        if c['classe'] == classe.capitalize(): 
            player1=criar_jogador(nome,c)
    
    
    escolha=input(f"Escolha apenas um dos equipamentos:\n 1- Poção da Vida (+10 saude) \n 2-Poção de Defesa (+10 defesa)\n 3-Poção de Ataque (+10 ataque)\n")
    match escolha:
        case "1":
            equipado=Vida(player1)
        case "2":
            equipado=Defesa(player1)
        case "3":
            equipado=Ataque(player1)
           
    print(equipado.status)
        
    
    print('NPCs')
    quantid=random.randint(0,len(lista)-1)
    inimigo1=lista[random.randint(0,quantid)]
    inimigo2=lista[random.randint(0,quantid)] 
    print(inimigo1)
    print(inimigo2)
        
    # cadeia de ataque
    fogo=FogoHandler()
    agua=AguaHandler()
    normal=NormalHandler()
    #ataques
    fogo.set_proximo(agua).set_proximo(normal)
    print(f"{Fore.LIGHTGREEN_EX}Inicio da Batalha{Style.RESET_ALL}")
    while inimigo1.saude > 0 and inimigo2.saude > 0 and player1.saude > 0:
            
        fogo.handle(inimigo1, player1)
    
        if player1.saude==0: break

        player1.atacar(inimigo1)
        
        
        if inimigo1.saude==0: break 
                
        fogo.handle(inimigo2,player1)
    
        if player1.saude==0: break
        
        player1.atacar(inimigo2)
    print(f"{Fore.LIGHTGREEN_EX}Fim da Batalha{Style.RESET_ALL}")
    print(f"Saude do(a) jogador(a) {player1.nome}:",player1.saude)
    print(f"Saude do {inimigo1.nome} de {inimigo1.elemento}:",inimigo1.saude)  
    print(f"Saude do {inimigo2.nome} de {inimigo2.elemento}:",inimigo2.saude)
        
