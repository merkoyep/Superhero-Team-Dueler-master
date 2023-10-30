import random
from ability import Ability
from armor import Armor
class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer'''

        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
       if not self.abilities and not opponent.abilities:
          print('Draw')
       else:
          game_status = True
          while game_status:
             opponent.take_damage(self.attack())
             self.take_damage(opponent.attack())
             if not self.is_alive() and not opponent.is_alive():
                print(f'Everyone died! It\'s a draw!')
                game_status = False
             elif not self.is_alive():
                print(f'{opponent.name} won!')
                game_status = False
             elif not opponent.is_alive():
                print(f'{self.name} won!')
                game_status = False
      #  weight_denominator = self.current_health + opponent.current_health
      #  self_ratio = self.current_health / weight_denominator * 100
      #  opponent_ratio = opponent.current_health / weight_denominator * 100
      #  winner = random.choices([self.name, opponent.name], [self_ratio, opponent_ratio])
      #  if winner[0] == self.name:
      #     loser = opponent.name
      #  else:
      #     loser = self.name
      #  print(f'{winner[0]} defeats {loser}!')
       
    def add_ability(self, ability):
       ''' Add ability to abilities list'''
       self.abilities.append(ability)
    def attack(self):
       '''calculate total damage from all ability attacks
       return: total_damage:Int'''

       total_damage = 0
       for ability in self.abilities:
          total_damage += ability.attack()
       return total_damage
    
    def add_armor(self, armor):
       '''Add armor to self.armors
       Armor: Armor Object'''
       self.armors.append(armor)

    def defend(self):
       '''Calculate the total block amount from all armor blocks.
     return: total_block:Int'''
       total_defense = 0
       for armor in self.armors:
          total_defense += armor.block()
       return total_defense

    def take_damage(self, damage):
       '''Updates self.current_health to reflect the damage minus the defense.'''
       if (damage - self.defend()) > 0:
          self.current_health -= (damage - self.defend())

    def is_alive(self):
       '''return True of False if hero is alive or not'''
       if self.current_health <= 0:
          return False
       else:
          return True
       

