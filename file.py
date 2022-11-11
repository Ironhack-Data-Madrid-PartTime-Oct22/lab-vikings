import vikingsClasses
#import Soldier 
#mport War 
import names ##generador aleatorio de nombres porque no me apetece pensar
import random
   
# creamos el ejercito de vikingos
v = int(input("number of vikings: "))
i = 0
armyViking = []
while i < v:
    viking = vikingsClasses.Viking(names.get_first_name(), random.randint(1, 300), random.randint(1, 300))
    print(viking.__dict__)
    testViking = vikingsClasses.War()
    armyViking.append(viking)
    i +=1
print(type(testViking), type(armyViking))

# creamos el ejercito de sajones
s = int(input("number of saxons: "))
i = 0
armySaxon = []
while i < s:
    saxon = vikingsClasses.Saxon(random.randint(1, 300), random.randint(1, 300))
    print(saxon.__dict__)
    testSaxon = vikingsClasses.War()
    armySaxon.append(saxon)
    i +=1
print(type(testSaxon), type(armySaxon))