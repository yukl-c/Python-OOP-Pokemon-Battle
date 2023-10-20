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
        self.lv = abilities['lv']
        self.attack = abilities['attack']
        self.defence = abilities['defence']
        self.speed = abilities['speed']
        self.hp = abilities['hp']
        self.attack_to_rival = 0

    #showing pokemon information
    def show(self, pokemon2):
        print('pokemon 1:',self.name,'\n','type:',self.types,'\n','lv:',self.lv,'\n','HP:',self.hp * "*",'\n')
        print('pokemon 2:',pokemon2.name,'\n','type:',pokemon2.types,'\n','lv:',pokemon2.lv,'\n','HP:',pokemon2.hp * "*",'\n')
        print("-" * 50)

    #calculating damage to target's pokemon
    def damage_to_rival(self, pokemon2):
        damage =int( 2 + (((2 * self.lv / 5) + 2 * self.move_power * (self.attack_to_rival  / pokemon2.defence)) / 50))
        return damage

    #giving command to pokemon
    def move_command(self):
        self.move_action = int(input('What is your action? \n'))
        self.move_name = self.moveList[self.move_action - 1]
        self.move_type = self.move[self.move_name]['Type']
        self.move_power = self.move[self.move_name]['Power']


    #calculating attack to target's pokemon from different types
    def attack_sum(self, pokemon2):
      #stronger attack types
      strongerAttackTypes = {
            'Fire': ['Grass', 'Ice', 'Flying'],
            'Water': ['Fire', 'Ground'],
            'Grass': ['Water', 'Ground'],
            'Ground': ['Fire', 'Electric'],
            'Ice': ['Grass', 'Flying'],
            'Electric': ['Water', 'Flying'],
            'Flying': ['Grass']
            }

      #weaker attack types
      weakerAttackTypes = {
            'Fire': ['Water', 'Ground','Fire'],
            'Water': ['Grass', 'Electric','Water'],
            'Grass': ['Fire', 'Flying', 'Electric'],
            'Ground': ['Grass'],
            'Ice': ['Ice', 'Fire', 'Water'],
            'Electric': ['Electric', 'Grass', 'Ground'],
            'Flying': ['Electric']
            }
      try:
        if (pokemon2.types in strongerAttackTypes[self.move_type]):
          self.attack_to_rival = self.attack * 2
          print("Its super effective!")
        elif (pokemon2.types in weakerAttackTypes[self.move_type]):
          self.attack_to_rival = int(self.attack * 0.5)
          print("Its not very effective...")
      except KeyError:
        self.attack_to_rival = self.attack

    #pokemon battle
    def fight(self, pokemon2):
      print('pokemon fight starts \n')
      self.show(pokemon2)

      Round = 1
      while ((self.hp > 0) and (pokemon2.hp > 0)):

            print('Round ',Round)
            print('Player 1', '\n', 'Go !',self.name,'\n',' move')
            for i, move in enumerate(list(self.move.items())):
                print(i+1, move)
            self.move_command()

            print('Player 2', '\n', 'Go !',pokemon2.name,'\n',' move')
            for i, move in enumerate(list(pokemon2.move.items())):
                print(i+1, move)
            pokemon2.move_command()

            if self.speed >= pokemon2.speed :
              #player 1 turn
              print(self.name, ' uses ', self.move_name, "! \n")
              self.attack_sum(pokemon2)
              #rival_hp_loss_from_self = self.damage_to_rival()
              pokemon2.hp -= self.damage_to_rival(pokemon2)
              self.show(pokemon2)
              if pokemon2.hp <= 0:
                  print('...',pokemon2.name,'fainted... /n')
                  print('Player 1 wins!')
                  break

              #player 2 turn
              print(pokemon2.name, ' uses ', pokemon2.move_name, "! \n")
              pokemon2.attack_sum(self)
              #rival_hp_loss_from_PM2 = pokemon2.damage_to_rival()
              self.hp -= pokemon2.damage_to_rival(self)
              self.show(pokemon2)
              if self.hp <= 0:
                  print('...',self.name,'fainted... /n')
                  print('Player 2 wins!')
                  break

            else:
              #player 2 turn
              print(pokemon2.name, ' uses ', pokemon2.move_name, "! \n")
              pokemon2.attack_sum(self)
              #rival_hp_loss_from_PM2 = pokemon2.damage_to_rival()
              self.hp -= pokemon2.damage_to_rival(self)
              self.show(pokemon2)
              if self.hp <= 0:
                  print('...',self.name,'fainted... /n')
                  print('Player 2 wins!')
                  break

              #player 1 turn
              print(self.name, ' uses ', self.move_name, "! \n")
              self.attack_sum(pokemon2)
              #rival_hp_loss_from_self = self.damage_to_rival()
              pokemon2.hp -= self.damage_to_rival(pokemon2)
              self.show(pokemon2)
              if pokemon2.hp <= 0:
                  print('...',pokemon2.name,'fainted... /n')
                  print('Player 1 wins!')
                  break
            Round = Round + 1
            print("=" * 50)




if __name__ == '__main__':
  Grookey = Pokemon('Grookey', 'Grass', {'Catch':{'Type':'Normal','Power':20}, 'Branch Poke':{'Type':'Grass','Power':40}}, {'lv': 5, 'attack':10, 'defence': 10, 'speed': 10, 'hp': 15})
  Scorbunny = Pokemon('Scorbunny', 'Fire', {'Kick':{'Type':'Normal','Power':20}, 'Ember':{'Type':'Fire','Power':40}}, {'lv': 5, 'attack':12, 'defence': 8, 'speed': 11, 'hp': 15})
  Sobble = Pokemon('Sobble', 'Water', {'Tackle':{'Type':'Normal','Power':20}, 'Water Gun':{'Type':'Water','Power':40}}, {'lv': 5, 'attack':11, 'defence': 9, 'speed': 12, 'hp': 15})

  Thwackey = Pokemon('Thwackey', 'Grass', {'Double Hit':{'Type':'Normal','Power':70}, 'Razor Leaf':{'Type':'Grass','Power':55}, 'Acrobatics':{'Type':'Flying','Power':55}}, {'lv': 20, 'attack':20, 'defence': 20, 'speed': 20, 'hp': 40})
  Raboot = Pokemon('Raboot', 'Fire', {'Double Kick':{'Type':'Normal','Power':70}, 'Flame Charge':{'Type':'Fire','Power':50}, 'Mud Shot':{'Type':'Ground','Power':55}}, {'lv': 20, 'attack':24, 'defence': 16, 'speed': 22, 'hp': 40})
  Drizzile = Pokemon('Drizzile', 'Water', {'Pound':{'Type':'Normal','Power':60}, 'Water Pulse':{'Type':'Water','Power':60}, 'Ice Shard':{'Type':'Ice','Power':60}}, {'lv': 20, 'attack':22, 'defence': 18, 'speed': 24, 'hp': 40})

  Rillaboom = Pokemon('Rillaboom', 'Grass', {'Slam':{'Type':'Normal','Power':80}, 'Wood Hammer':{'Type':'Grass','Power':90}, 'Acrobatics':{'Type':'Flying','Power':55}, 'Earthquake':{'Type':'Ground','Power':100}}, {'lv': 35, 'attack':33, 'defence': 33, 'speed': 24, 'hp': 60})
  Cinderace = Pokemon('Cinderace', 'Fire', {'Headbutt':{'Type':'Normal','Power':70}, 'Flame Ball':{'Type':'Fire','Power':100}, 'Mud Shot':{'Type':'Ground','Power':55}, 'Electro Ball':{'Type':'Electirc','Power':100}}, {'lv': 35, 'attack':37, 'defence': 21, 'speed': 35, 'hp': 60})
  Inteleon = Pokemon('Inteleon', 'Water', {'Swift':{'Type':'Normal','Power':60}, 'Liquidation':{'Type':'Water','Power':85}, 'Ice Shard':{'Type':'Ice','Power':60}, 'Air Cutter':{'Type':'Flying','Power':60}}, {'lv': 35, 'attack':33, 'defence': 27, 'speed': 36, 'hp': 60})

  Pikachu = Pokemon('Pikachu', 'Electric', {'Thunderbolt':{'Type':'Electric','Power':90}, 'Dig':{'Type':'Ground','Power':80}, 'Surf':{'Type':'Water','Power':90}, 'Fly':{'Type':'Flying','Power':90}}, {'lv': 35, 'attack':29, 'defence': 27, 'speed': 40, 'hp': 60})

  Scorbunny.fight(Inteleon)

