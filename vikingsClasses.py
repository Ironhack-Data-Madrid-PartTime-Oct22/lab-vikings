
# Soldier


class Soldier:
    def __init__(self,health,strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health-=damage
  


# Viking


class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name = name

    def receiveDamage(self,damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"



# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength) 
    def receiveDamage(self,damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"



# War

import random
import numpy as np

class War():
    vikingArmy=np.array([]) #esto lo he sacado de la leccion de Numpy
    saxonArmy=np.array([])
        
    def addViking(Viking): #se que no funciona este append argg me estoy rallando mucho
        vikingArmy.append(Viking) #si pongo aqui Viking me lee la clase??

    def addSaxon(Saxon):
        saxonArmy.append(Saxon)
        
    random_viking=random.choice(vikingArmy)#tampoco me funciona random
    random_saxon=random.choice(saxonArmy)
         
    def vikingAttack(): #esto lo he hecho un poco como he podido pero se que no funciona !! estoy lost con este ejercicio :( correccion plzzzz

        def receiveDamage(self,damage=random_saxon.strength):
            random_viking.self.health-=self.damage
            if random_viking.self.health<=0:
                vikingArmy.remove(random_viking)
            else:
                return random_viking.self.health

    def saxonAttack():
        def receiveDamage(self,damage=random_viking.strength):
            random_saxon.self.health-=self.damage
            if random_viking.self.health<=0:
                saxonArmy.remove(random_viking)
            else:
                return random_saxon.self.health

    def showStatus():
        empty_list=[]
        if vikingArmy==empty_list:
            return "Saxons have fought for their lives and survive another day..."
        elif saxonArmy==empty_list:
            return "Vikings and Saxons are still in the thick of battle."

            """buaa lo he hecho fatal :( sobre todo me he liado con el principio, no se como meter los viking y saxons en los arrays.
            Me parece un ejercicio guay y quiero entenderlo, con las correciones lo revisaré""
        
