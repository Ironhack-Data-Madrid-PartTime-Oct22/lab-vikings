
from vikingsClasses import War
from vikingsClasses import Viking
from vikingsClasses import Saxon

class Game(War):

    def reclutamiento(self):

        import random

        participantes = int(input("Intrdozuzca el numero de participantes: \n"))

        strength = random.randint(60,100)

        for i in range(0, (participantes + 1)):
            equipo = random.randint(1,2)

            if equipo == 1:

                if len(self.vikingArmy) != (participantes/2):
                    name = input("Intrdozuzca el nombre del jugador: \n")
                    soldado = Viking(name, random.randint(60,100), random.randint(10,20))
                    War.addViking(self, soldado)

                else:
                    if len(self.saxonArmy) != (participantes/2):
                        soldado = Saxon(random.randint(60,100), random.randint(10,20))
                        War.addSaxon(self, soldado)
                        print("Saxon:",soldado.__dict__)

            elif equipo == 2:

                if len(self.saxonArmy) != (participantes/2):
                    soldado = Saxon(random.randint(60,100), random.randint(10,20))
                    War.addSaxon(self, soldado)
                    print("Saxon:",soldado.__dict__)

                else:
                    if len(self.vikingArmy) != (participantes/2):
                        name = input("Intrdozuzca el nombre del jugador: \n")
                        soldado = Viking(name, random.randint(60,100), random.randint(10,20))
                        War.addViking(self, soldado)

        return "Los ejercitos estan listos.\n"

    
    def play(self):

        cont=0
        ganador = 0
        while ganador < 1:
            if cont == 0 :
                print("Empieza el combate gerreros.\n")

            elif cont > 1 and cont < 15:
                print("Una batalla más para llegar a la gloria.\n")

            else:
                print("Parece que la batalla se esta extendiendo más de lo necesario.\n")

            if len(self.vikingArmy) != 0:
                print("Atacan los vikingos")
                print(War.vikingAttack(self))
            else:
                ganador+= 1

            print("\n")

            if len(self.saxonArmy) != 0: 
                print("Atacan los sajones")
                print(War.saxonAttack(self))
            else:
                ganador+= 1

            print(War.showStatus(self))

            cont+= 1
        return "Ha sido una gran batalla."

juego = Game()
print(juego.reclutamiento())
print(juego.play())


