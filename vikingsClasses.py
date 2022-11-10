
# Soldier


class Soldier:
    def __init__(self, health, strength):

       self.health = health
       self.strenght = strength

    def attack(self):
        return {self.strenght}
    
    def receiveDamage(self, damage):
        
        self.damage = damage

        {self.health} - {damage}
        
        


# Viking


class Viking(Soldier):

    

# Saxon


class Saxon:
    pass

# War


class War:
    pass
