from models import (NPC, Mage, Dragon, Player, Mario, Joker)
from random import randint
def create_NPC() -> NPC:
    num=randint(1,2)
    if num==1: 
        return Dragon() 
    elif num==2: 
        return Mage() 
    
def create_Player() -> Player:
    num=randint(1,2)
    if num==1: 
        return Mario() 
    elif num==2: 
        return Joker()
    
