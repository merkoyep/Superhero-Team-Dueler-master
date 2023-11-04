import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
        abilities: List
        armors: List
        name: String
        starting_health: Integer
        current_health: Integer'''
        self.deaths = 0
        self.kills = 0
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def fight(self, opponent):
       if not self.abilities and not opponent.abilities:
          return 'Draw'
       else:
          game_status = True
          while game_status:
             opponent.take_damage(self.attack())
             self.take_damage(opponent.attack())
             if not self.is_alive() and not opponent.is_alive():
                game_status = False
                print(f'Everyone died! It\'s a draw!')
                return 'Tie'
             elif not self.is_alive():
                opponent.add_kill(1)
                self.add_death(1)
                game_status = False
                print(f'{opponent.name} won!')
                return 'Lose'
             elif not opponent.is_alive():
                self.add_kill(1)
                opponent.add_death(1)
                game_status = False
                print(f'{self.name} won!')
                return 'Win'
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
    def add_weapon(self, weapon):
       self.abilities.append(weapon)

    def add_kill(self, num_kills):
       '''Update self.kills by num_kills amount'''
       self.kills += num_kills
    def add_death(self, num_deaths):
       '''update deaths with num_deaths'''
       self.deaths += num_deaths

    