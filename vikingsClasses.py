# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    ##metodo01: attack, definido
    def attack(self):
        return self.strength
    ##metodo02: receiveDamage, se hace pupa --> ojo con el self the damage
    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    ##metodo01: attack, no hay que definirlo, heredado
    ##metodo02: receiveDamage, se hace pupa --> ojo con el self the damage
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
    #metodo03: unga unga unga
    def battleCry(self):
        return "Odin Owns You All!"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    ##metodo01: attack, no hay que definirlo, heredado
    ##metodo02: receiveDamage, se hace pupa --> ojo con el self the damage
    def receiveDamage(self, damage):
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

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        import random ## para seleccionar a un muembro random de cada ejército
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        random_saxon.receiveDamage(random_viking.strength)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return random_saxon.receiveDamage(random_viking.strength)
    
    def saxonAttack(self):
        import random ## para seleccionar a un muembro random de cada ejército
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return random_viking.receiveDamage(random_saxon.strength)
    
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy)  >0 and len(self.vikingArmy) > 0:
            return f"Vikings and Saxons are still in the thick of battle."

