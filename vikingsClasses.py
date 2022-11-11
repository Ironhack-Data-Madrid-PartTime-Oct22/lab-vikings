
# Soldier


class Soldier:
    #Definimos la clase Soldiers con los atributos Health y Strength
    def __init__ (self, health, strength):
        self.health=health
        self.strength=strength
    #Creamos metodo 'Attack' que nos devuelve la fuerza
    def attack(self):
        return self.strength
    #Creamos metodo 'Receive Damage' que nos pide un argumento, el 'Damage'. La función resta del atributo Health el argumento Damage
    def receiveDamage(self,damage):
        self.health-=damage

# Viking


class Viking(Soldier):
    #Definimos una hija de Soldiers llamada Viking y le añadimos un atributo nuevo, Name
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name=name

    ##Creamos metodo 'Receive Damage' que nos pide un argumento, el 'Damage'. La función resta del atributo Health el argumento Damage
    #Si la Health es mayor que cero nos devuelve una frase, y en el resto de supuestos, nos devuelve otra
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    #Añadimos el metodo battleCry que devuelve el grito de batalla
    def battleCry(self):
        return "Odin Owns You All!"
    
    

# Saxon

#Creamos una nueva subclase de Soldiers, Saxon
class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__(health, strength)
    ##Creamos metodo 'Receive Damage' que nos pide un argumento, el 'Damage'. La función resta del atributo Health el argumento Damage
    #Si la Health es mayor que cero nos devuelve una frase, y en el resto de supuestos, nos devuelve otra    
    def receiveDamage(self,damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"
   

# War
#TUVE QUE BUSCAR POR INTERNET. UNA VEZ VISTO, LO ENTIENDO Y TIENE SENTIDO.
import random 
#Importamos random ya que nos tocará usarlo luego
class War:#Creamos una nueva clase, War
    #No tiene ningún atributo, pero hay que añadirle dos listas vacias ara cada uno de los ejercitos
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        #PREGUNTA, TODO LO QUE VAYA AQUÍ DEBE LLEVAR EL SELF SI SE VA A USAR LUEGO, VERDAD? AL PRINCIPIO NO SE LO PUSE Y ME COSTÓ DARME CUENTA. PENSABA QUE ERA SOLO PARA LOS ATRIBUTOS
    #Añadimos el método add Viking con un solo parametro. Añade 1 Viking al Viking Army
    def addViking(self,Viking):
        self.viking=Viking
        self.vikingArmy.append(Viking)
    #Lo mismo con los Saxon
    def addSaxon(self,Saxon):
        self.Saxon=Saxon
        self.saxonArmy.append(Saxon)
    #AQUÍ NO SE ME OCURRIÓ EL CREAR VARIABLE NUEVAS. ESTABA EMPEÑADA EN HACERLO TODO CON LO YA EXISTENTE Y OBVIAMENTE NO HABÍA MANERA
    #LO QUE ESTABA INTENTANDO MÁS O MENOS ERA:
    """"Saxon.receiveDamage(Viking.attack) y no dejaba de darme el error. Entiendo que tienes que crear variables ya que Saxon o Viking son nombres de clases, no elementos. ¿Es así? """
    def vikingAttack(self):
        random_viking=random.choice(self.vikingArmy)
        random_saxon=random.choice(self.saxonArmy)
        damage_saxon=random_saxon.receiveDamage(random_viking.attack())#PREGUNTA: Por qué se ponen los paréntesis después de attack?
        #Aquí igual, me estaba empecinando en conseguir la salud de Saxon (Saxon.health) pero no podía acceder. Aunque en el fondo estamos haciendo algo parecido no? 
        #El random saxon es un saxon cualquiera de la lista, si podemos acceder a su salud a traves de apendizarlo (se dice asi?), por que no me dejaba hacerlo a Saxon directamente?
        #Si la salud del random saxon es menor o igual que cero, lo removemos de la lista del ejercito
        #Finalmente pedimos que nos devuelva el daño recibido, que activa el metodo 'receive damage' y utiliza el metodo attack de Viking(Soldier) como argumento, sustituyendo así al damage
        if random_saxon.health<=0:
            self.saxonArmy.remove(random_saxon)
        return damage_saxon
    #Igual que el anterior pero para los saxons
    def saxonAttack(self):
        random_vik=random.choice(self.vikingArmy)
        random_sax=random.choice(self.saxonArmy)
        damage_vik=random_vik.receiveDamage(random_sax.attack())
        
        if random_vik.health<=0:
            self.vikingArmy.remove(random_vik)
        return damage_vik
    #Y por fin la parte fácil, añadimos otro metodo que comprueba la longitud de los ejercitos y dependiendo de cual llegue a cero da un resultado u otro. En el resto de los caso, dice otra cosa
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

    #Las tres primeras clases fueron sin problema, pero esta última, sino hubiera sido por google dudo que la hubiera sacado. El bonus ya si eso, para otro día que la cabeza ya no sabe donde está
        