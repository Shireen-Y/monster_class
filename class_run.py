# Import stuff here
from class_monster import *

monster1 = Monster('Paul', skills)

# Testing scare_attack()

print('checking if monster can scare_attack properly')
print(monster1.scare_attack() == 'RAAAAHH')

print('checking if monster can sleep properly')
print(monster1.sleep() == 'zzzzzz')

print('checking if monster can eat properly')
print(monster1.eat() == 'NOM NOM NOM!')

