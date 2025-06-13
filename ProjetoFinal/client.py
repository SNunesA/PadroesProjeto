import json
from abstractfactory import *


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
    
for c in lista: print(c)
        
    