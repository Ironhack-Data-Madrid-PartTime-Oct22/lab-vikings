
# Soldier

class Soldier:
    def __init__(self, health, strength):

        self.health =health
        self.strength =strength
    
    
    def attack(self):

        return self.strength
    
    
    def receiveDamage(self, strength):

        self.health -= strength
        

# Viking

class Viking(Soldier):

    def __init__(self, name, health, strength):

        self.name = name
        super().__init__(health, strength)
    
    
    def receiveDamage(self, strength):

        self.health -= strength

        if self.health > 1:
            return f"{self.name} has received {strength} points of damage"
        
        else:
            return f"{self.name} has died in act of combat"
    

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):

    def __init__(self, health, strength):

        super().__init__(health, strength)
    
    
    def receiveDamage(self, strength):

        self.health -= strength

        if self.health > 1:
            return f"A Saxon has received {strength} points of damage"
        
        else:
            return "A Saxon has died in combat"


# War

class War():

    def __init__(self):

        self.vikingArmy= []
        self.saxonArmy= []
        
    def addViking(self, Viking):

        
        self.vikingArmy.append(Viking)


    def addSaxon(self, Saxon):

        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random

        viking = self.vikingArmy[random.randint(0, (len(self.vikingArmy)-1))]
        saxon = self.saxonArmy[random.randint(0, (len(self.saxonArmy)-1))]
        
        resultado = saxon.receiveDamage(viking.strength)

        if saxon.health < 1:
            self.saxonArmy.pop(self.saxonArmy.index(saxon))
        return resultado


    def saxonAttack(self):
        import random

        viking = self.vikingArmy[random.randint(0, (len(self.vikingArmy)-1))]
        saxon = self.saxonArmy[random.randint(0, (len(self.saxonArmy)-1))]
        
        resultado = viking.receiveDamage(saxon.strength)

        if viking.health < 1:
            self.vikingArmy.pop(self.vikingArmy.index(viking))

        return resultado


    def showStatus(self):

        if len(self.vikingArmy) < 1:
            return "Saxons have fought for their lives and survive another day..."

        elif len(self.saxonArmy) < 1:
            return "Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) and len(self.saxonArmy) != 0:
            return "Vikings and Saxons are still in the thick of battle."