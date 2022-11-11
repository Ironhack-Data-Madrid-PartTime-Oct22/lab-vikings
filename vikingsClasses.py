
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        attack = self.strength 
        return self.strength
    def receivedDamage(self,receivedDamage = int(input(f'introduce el daño recibido ----> '))):
            self.health -= receivedDamage 
sol1 = Soldier(500,250)


sol1
# Viking


class Viking(Soldier):
      def __init__(self,name, health, strength):
        super().__init__( health, strength)
        self.name = name
        self.health = health
        self.strength = strength
      
      def receivedDamage(self):
            receivedDamage = int(input(f'introduce el daño recibido ----> '))
            self.health -= receivedDamage
            if self.health > 0:
                 return f'{self.name} has received {self.receivedDamage} points of damage'
                
            else:
                 return f'{self.name} has died in act of combat'    
                
      
      def battleCry(self):
            return f'Odin Owns You All!'








# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        self.health = health
        self.strength = strength
    def receivedDamage(self):
            receivedDamage = int(input(f'introduce el daño recibido ----> '))
            self.health -= receivedDamage 
            if self.health > 0:
                 return f'Saxon has received {self.receivedDamage} points of damage'
                
            else:
                 return f'Saxon has died in act of combat'    



# War
class War:
    vikingArmy =[]
    saxonArmy = []
    
    def addViking(Viking):
        vik = Viking()
        vikingArmy.add(vik) 
    
    def addSaxon(Saxon):
        sax = Saxon()
        saxonArmy.add(sax)
        
    def vikingAttack(Viking):
           def receivedDamage(self):
            receivedDamage = Saxon.strength
            self.health -= receivedDamage
            if self.health > 0:
                 return f'{self.name} has received {self.receivedDamage} points of damage'
                
            else:
                 return f'{self.name} has died in act of combat' 
    
    
    def saxonAttack(Saxon):
        def receivedDamage(self):
            receivedDamage = Viking.strenght
            self.health -= receivedDamage 
            if self.health > 0:
                 return f'Saxon has received {self.receivedDamage} points of damage'
                
            else:
                 return f'Saxon has died in act of combat'    
    def showStatus:
