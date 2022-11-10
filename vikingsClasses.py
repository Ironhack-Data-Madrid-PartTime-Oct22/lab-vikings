
# Soldier


class Soldier:
    def __init__ (self, health, strength):
        self.health=health
        self.strength=strength

    def attack(self):
        return self.strength
    def receiveDamage(self,damage):
        self.health-=damage

# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name=name

   
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin Owns You All!"
    
    

# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__(health, strength)
        

    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
    pass

# War


class War():

    class War(Saxon):
        def __init__ (self, health, strength):
        super().__init__(health, strength)




    def __init__ (self):
        self.vikingArmy=list()
        self.saxonArmy=list()
    

    def addViking(self,Viking):
        self.Viking=Viking
        self.vikingArmy.extend("1")
        

    def addSaxon(self,Saxon):
        self.Saxon=Saxon
        self.saxonArmy.extend("1")

          

    def vikingAttack(self):
        Saxon.receiveDamage-=Viking.
        if Saxon.health<0:
            self.saxonArmy.pop()
        return f"result of calling {Saxon.receiveDamage} of a {Saxon} with the {strength} of a {Viking}"
    def saxonAttack(self):
        Viking.receiveDamage-=Saxon.s
        if Viking.health<0:
            self.vikingArmy.pop()
        return f"result of calling {Viking.receiveDamage} of a {Viking} with the {strength} of a {Saxon}"
    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    pass
