
# Soldier

class Soldier:

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength 
    
    def attack(self):
        return{self.strength}
    
    def receiveDamage(self,damage):

        return self.health -= damage

soldado= Soldier(300,150) 

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name= name
        self.health = health
        self.strength = strength  
    
    def attack(self):
        return{self.strength}

    def receiveDamage(self,damage):

        if self.health-damage <=0 :
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"

    def battleCry(self):
            return "Odin Owns You All!"

vikingo= Viking("Loki", 150, 90)

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength  
    
    def attack(self):
        return{self.strength}

    def receiveDamage(self,damage):

        if self.health-damage <=0 :
            return f"Saxon has died in act of combat"
        else:
            return f"Saxon has received {damage} points of damage"
    pass

    sancho= Saxon(100, 50) 

# War


class War:
    pass
