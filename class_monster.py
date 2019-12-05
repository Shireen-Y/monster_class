# Define monster and methods here

class Monster():
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills

    def sleep(self):
        return 'zzzzzz'
    def eat(self):
        return 'NOM NOM NOM!'
    def scare_attack(self):
        return 'RAAAAHH'

skills = ['scary', 'hairy', 'loud']
