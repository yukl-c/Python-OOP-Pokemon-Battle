###Pokemon Battle Class

class Pokemon():
    def __init__(self, name, types, move, abilities):
        self.name = name
        self.types = types
        self.move = move
        self.moveList = list(self.move.keys())
        self.move_type = ''
        self.move_name = ''
        self.move_action = ''
        self.move_power = ''
        self.attack = abilities['attack']
        self.defence = abilities['defence']
        self.speed = abilities['speed']
        self.hp = abilities['hp']
        self.attack_to_rival = 0

    def show(self, pokemon2):
        print('pokemon 1:',self.name,'\n','type:',self.types,'\n','HP:',self.hp * "*",'\n')
        print('pokemon 2:',pokemon2.name,'\n','type:',pokemon2.types,'\n','HP:',pokemon2.hp * "*",'\n')
        
    def hp_defence(self):
        for i in range(int(self.hp + 0.01*self.defence)):
            self.hp += 1
        return self.hp

    def move_command(self):
            self.move_action = int(input('What is your action? '))
            self.move_name = self.moveList[self.move_action - 1]
            self.move_type = self.move[self.move_name]['Type']
            self.move_power = self.move[self.move_name]['Power']        

    def fight(self, pokemon2):
        strongerAttackTypes = {
            'Fire': ['Grass', 'Ice', 'Flying'],
            'Water': ['Fire', 'Ground'],
            'Grass': ['Water', 'Ground'],
            'Ground': ['Fire', 'Electric'],
            'Ice': ['Grass', 'Flying'],
            'Electric': ['Water', 'Flying'],
            'Flying': ['Grass']
            }

        weakerAttackTypes = {
            'Fire': ['Water', 'Ground','Fire'],
            'Water': ['Grass', 'Electric','Water'],
            'Grass': ['Fire', 'Flying', 'Electric'],
            'Ground': ['Grass'],
            'Ice': ['Ice', 'Fire', 'Water'],
            'Electric': ['Electric', 'Grass', 'Ground'],
            'Flying': ['Electric']
            }
        
        print('pokemon fight starts \n')
        self.show(pokemon2)

        while ((self.hp > 0) and (pokemon2.hp > 0)):
            Round = 1
            print('Round ',Round)
            print('Player 1', '\n', self.name,' move')
            for i, move in enumerate(self.moveList):
                print(i+1, move)
##            self.move_action = int(input('What is your action? '))
##            self.move_name = self.moveList[self.move_action - 1]
##            self.move_type = self.move[self.move_name]['Type']
##            self.move_power = self.move[self.move_name]['Power']
            self.move_command()
            
            print('Player 2', '\n', pokemon2.name,' move')
            for i, move in enumerate(PM2_moveList):
                print(i+1, move)
##            pokemon2.move_action = int(input('What is your action? '))
##            pokemon2.move_name = pokemon2.moveList[pokemon2.move_action - 1]
##            pokemon2.move_type = pokemon2.move[pokemon2.move_name]['Type']
##            pokemon2.move_power = pokemon2.move[pokemon2.move_name]['Power']
            pokemon2.move_command()

##            if self.speed >= pokemon2.speed :
##                try:
##                    if (pokemon2.types in strongerAttackTypes[PM1_move_type]):
##                        attack_to_PM2 = self.attack * 2
##                    elif (pokemon2.types in weakerAttackTypes[PM1_move_type]):
##                        attack_to_PM2 = round(self.attack * 0.5)
##                except KeyError:
##                    attack_to_PM2 = self.attack
##                print(attack_to_PM2)
##                pokemon2.hp -= attack_to_PM2
##                print(pokemon2.hp)
##                pokemon2.hp += pokemon2.hp_defence()
##                print(pokemon2.hp)
##                self.show(pokemon2)
##                if pokemon2.hp <= 0:
##                    print('end game! /n')
##                    print('Player 1 wins!')
##                    break
##                
##                try:
##                    if (self.types in strongerAttackTypes[PM2_move_type]):
##                        self.attack_to_rival = pokemon2.attack * 2
##                    elif (self.types in weakerAttackTypes[PM2_move_type]):
##                        self.attack_to_rival = round(pokemon2.attack * 0.5)
##                except KeyError:
##                    self.attack_to_rival = pokemon2.attack
##                print(self.attack_to_rival)
##                self.hp -= attack_to_PM1
##                print(self.hp)
##                self.hp += self.hp_defence()
##                print(self.hp)
##                self.show(pokemon2)
##                if self.hp <= 0:
##                    print('end game! /n')
##                    print('Player 2 wins!')
##                    break
##
##            else:
##                try:
##                    if (self.types in strongerAttackTypes[PM2_move_type]):
##                        attack_to_PM1 = pokemon2.attack * 2
##                    elif (self.types in weakerAttackTypes[PM2_move_type]):
##                        attack_to_PM1 = round(pokemon2.attack * 0.5)
##                except KeyError:
##                    attack_to_PM1 = pokemon2.attack
##                print(attack_to_PM1)
##                self.hp -= attack_to_PM1
##                print(self.hp)
##                self.hp += self.hp_defence()
##                print(self.hp)
##                self.show(pokemon2)
##                if self.hp <= 0:
##                    print('end game! /n')
##                    print('Player 2 wins!')
##                    break
##
##                try:
##                    if (pokemon2.types in strongerAttackTypes[PM1_move_type]):
##                        attack_to_PM2 = self.attack * 2
##                    elif (pokemon2.types in weakerAttackTypes[PM1_move_type]):
##                        attack_to_PM2 = round(self.attack * 0.5)
##                except KeyError:
##                    attack_to_PM2 = self.attack
##                print(attack_to_PM2)
##                pokemon2.hp -= attack_to_PM2
##                print(pokemon2.hp)
##                pokemon2.hp += pokemon2.hp_defence()
##                print(pokemon2.hp)
##                self.show(pokemon2)
##                if pokemon2.hp <= 0:
##                    print('end game! /n')
##                    print('Player 1 wins!')
##                    break
                
            Round += 1

            
            

                
Charmander = Pokemon('Charmander', 'Fire', {'Catch':'Normal', 'Ember':'Fire'}, {'attack':12, 'defence': 8, 'speed': 10, 'hp': 20})
Squirtle = Pokemon('Squirtle', 'Water', {'Tackle':'Normal', 'Water Gun':'Water'}, {'attack':10, 'defence': 12, 'speed': 8, 'hp': 20})

##Charmander.fight(Squirtle)
##print(list(Charmander.move.keys())[0])

print(Charmander.moveList)
