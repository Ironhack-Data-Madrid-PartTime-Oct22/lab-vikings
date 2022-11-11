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
    ##metodo01: addViking, añade elementos de la subclase Vikings a mi éjercito
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    ##metodo02: addSaxon, añade elementos de la subclase Saxons a mi éjercito
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    ##metodo03: ataqueVikingo, la salud del atacado se resta según la fuerza del oponente
    ##si muere, me lo quito del ejército
    def vikingAttack(self):
        import random ## para seleccionar a un muembro random de cada ejército
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        resultado = random_saxon.receiveDamage(random_viking.strength) ##ojo, si lo hago igual a receivDamage() ya me da todos los valores del daño que he definido antes
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
            #return f"A Saxon has died in combat"
        return resultado
    ##metodo04: ataqueVikingo, la salud del atacado se resta según la fuerza del oponente
    ##si muere, me lo quito del ejército
    def saxonAttack(self):
        import random ## para seleccionar a un muembro random de cada ejército
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        resultado = random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
            #return f"{random_viking.name} has died in act of combat"
        return resultado
    ##metodo05: checkea si quedan miembros en las listas éjercitos, sino ya acaba
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            return f"Vikings and Saxons are still in the thick of battle."

