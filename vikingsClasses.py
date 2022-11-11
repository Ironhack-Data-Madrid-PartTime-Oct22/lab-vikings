import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self,damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self,name,health,strength):
        super().__init__(health,strength)
        self.name = name

    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return f"Odin Owns You All!"  
    
# Saxon


class Saxon(Soldier):
    def __init__(self,health,strength):
        super().__init__(health,strength)
    
    def receiveDamage(self,damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died in combat"

# War

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        rand_Saxon = (random.choice(self.saxonArmy))
        rand_Viking = (random.choice(self.vikingArmy))
        damage = rand_Viking.strength
        aftermath = rand_Saxon.receiveDamage(damage)
        if rand_Saxon.health <= 0:
            self.saxonArmy.pop()
        return aftermath

    def saxonAttack(self):
        rand_Saxon = (random.choice(self.saxonArmy))
        rand_Viking = (random.choice(self.vikingArmy))
        damage = rand_Saxon.strength
        aftermath = rand_Viking.receiveDamage(damage)
        if rand_Viking.health <= 0:
            self.vikingArmy.pop()
        return aftermath
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) and len(self.vikingArmy) >=1:
            return f"Vikings and Saxons are still in the thick of battle."
