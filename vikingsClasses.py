
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"   

# War
# Sorry, llevo probándolo bastante rato y no me sale :(


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        Saxon.receiveDamage(self, damage = self.strength(Viking))
        if self.health(Saxon) < 0:
            self.saxonArmy.pop()
        return self.receiveDamage(self, damage = self.strength(Viking))

    def saxonAttack(self):
        Viking.receiveDamage(self, damage = self.strength(Saxon))
        if self.health(Viking) < 0:
            self.vikingArmy.pop()
        return self.receiveDamage(self, damage = self.strength(Saxon)) 

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return "Vikings and Saxons are still in the thick of battle."
        
