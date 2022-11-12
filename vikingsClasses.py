
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health 
        self.strength = strength
# method1:  it returns the strength property of the Soldier
    def attack (self):
        return self.strength
# method 2 : it removes the received damage from the `health` property
    def receiveDamage(self,damage):
        self.health-=damage 

# Viking

class Viking (Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name

    def attack (self):
        return self.strength

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!" 


# Saxon

class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War

class War:
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        import random 
        sax= random.choice(self.saxonArmy)
        vik= random.choice(self.vikingArmy)
        resultado= sax.receiveDamage(vik.strength)
        if sax.health<=0:
            self.saxonArmy.remove(sax)
        return resultado

    def saxonAttack(self):
        import random 
        sax= random.choice(self.saxonArmy)
        vik= random.choice(self.vikingArmy)
        resultado= vik.receiveDamage(sax.strength)
        if vik.health<=0:
            self.vikingArmy.remove(vik)
        return resultado

    def showStatus(self):
        if len(self.saxonArmy) ==0 :
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) ==0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) ==1 and len(self.vikingArmy) ==1 :
            return "Vikings and Saxons are still in the thick of battle."





    
