import random

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
    def fight(self, opponent):
       weight_denominator = self.current_health + opponent.current_health
       self_ratio = self.current_health / weight_denominator * 100
       opponent_ratio = opponent.current_health / weight_denominator * 100
       winner = random.choices([self.name, opponent.name], [self_ratio, opponent_ratio])
       if winner[0] == self.name:
          loser = opponent.name
       else:
          loser = self.name
       print(f'{winner[0]} defeats {loser}!')
       

if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
  hero1 = Hero("Wonder Woman")
  hero2 = Hero("Dumbledore")

  hero1.fight(hero2)

