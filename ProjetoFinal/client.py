import json
from abstractfactory import (AguaFactory,FogoFactory)
from builder import PlayerBuilder
from decoratorequip import (Vida,Defesa,Ataque) 
from chainresponsability import(FogoHandler,AguaHandler, NormalHandler)

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
    for c in lista: 
        print(c)
        
    
    inimigo1=lista[0]
    inimigo2=lista[1] 
        
        
    # cadeia de ataque
    fogo=FogoHandler()
    agua=AguaHandler()
    normal=NormalHandler()
    #ataques
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
    print(f"Saude do {inimigo1.nome} de {inimigo1.elemento}:",inimigo1.saude)  
    print(f"Saude do {inimigo2.nome} de {inimigo2.elemento}:",inimigo2.saude)
        
