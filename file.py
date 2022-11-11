from vikingsClasses import Soldier, Viking, Saxon, War
#import Soldier 
#mport War 
import names ##generador aleatorio de nombres porque no me apetece pensar
import random

## axiona a tomar --> entiendo que es como cuando haces pd.read_csv()
war = War()

# creamos el ejercito de vikingos
v = int(input("number of vikings: "))
i = 1
while i <= v:
    viking = Viking(names.get_first_name(), random.randint(0, 300), random.randint(0, 300))
    print(f"vikingo numero {i}:", viking.__dict__)
    war.addViking(viking)
    i +=1

# creamos el ejercito de sajones
s = int(input("number of saxons: "))
i = 1
while i <= s:
    saxon = Saxon(random.randint(1, 300), random.randint(1, 300))
    print(f"sajón numero {i}:", saxon.__dict__)
    war.addSaxon(saxon)
    i +=1

## a pegarse por rondas
count = 0
rounds = int(input("cuantas rondas quieres que dure la guerra: "))
while count < rounds:
    war.vikingAttack()
    war.saxonAttack()
    check = war.showStatus()
    print(check)
    count +=1

## a pegarse a muerte
while len(war.vikingArmy) != 0 or len(war.saxonArmy) != 0:
    war.vikingAttack()
    war.saxonAttack()
    check = war.showStatus()
    print(check)
    if len(war.vikingArmy) == 0 or len(war.saxonArmy) == 0:
        break ##si ganan los sajones, no se rompe, si ganan los vikingos se rompe todo