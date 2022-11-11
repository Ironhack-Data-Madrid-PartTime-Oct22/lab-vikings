
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
        
    def receiveDamage(self, damage):
        self.health -= damage

# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        super().__init__(health, strength,)

    def receiveDamage(self, damage):
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
        super().__init__(health, strength,)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died in combat"

# War


class War():

        vikingArmy = []
        saxonArmy = []
    
    def addViking(self, Viking): #no entiendo bien como me va a coger la helth y fuerza del vikingo
        # se me ocurre meter un diccionario a la lista
        # pero luego el saxon y el vikingo tienen parametros distintos...
        for i in vikingArmy:
            vickingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        for s in vikingArmy:
            saxonArmy.append(Saxon)
    
    def vikingAttack():
# should make a Saxon receiveDamage() equal to the strength of a Viking
# priemeo tengo que escoger a un vikingo random de la lista army
        receiveDamage(self.Viking) == strenght(Viking) # aqui veo la utilidad del dic porq sino como meto la strength...
        return receiveDamage(self.Viking) -= strenght(Viking)

    def saxonAttack():
        return

    def showStatus(self):
        if len(saxonArmy)==0:
            retrun f"Vikings have won the war of the century!"
        elif len(vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

