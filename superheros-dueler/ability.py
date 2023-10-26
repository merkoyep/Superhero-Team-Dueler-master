import random

class Ability:
  def __init__(self, name, max_damage):
    '''
    Initialize the values passed into this
    method as instance variables.
    '''

    # Assign the "name" and "max_damage"
    # for a specific instance of the Ability class
    self.name = name
    self.max_damage = max_damage

  def attack(self):
    '''Returns a value between 0 and the max damage dealt by the ability'''
    attack_value = random.randint(0, self.max_damage)
    return attack_value
  

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.