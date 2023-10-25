# Create the Arena

We need a place for our heroes to duke it out, otherwise who's gonna pay for all that damage to the cities?

This chapter will have you doing a bit more of the coding on your own than the previous ones have. However, you'll be using a lot of your existing code here to build out the Arena class.

Let's build out the last phase of our superhero team dueler project!

# Creating the Battle Arena

Our heroes need somewhere to battle. let's have our user create our heroes with all of their respective gear and abilities. Our arena will take care of creating heroes and adding them to their respective teams.

Let's create some methods in an Arena class that  will allow for code reuse. Use your favorite loops with the `input()` function to build teams based on user input.

In your project directory, create a new file named `arena.py` to contain the arena class

Start by making an `init` method for your Arena class. Follow the TODO comment, you shouldn't be adding more than 2 lines of code here:

**HINT:** Remember how you create other objects(like ability).

```python
from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
  def __init__(self):
    '''Instantiate properties
        team_one: None
        team_two: None
    '''
    # TODO: create instance variables named team_one and team_two that
    # will hold our teams.
```

<!-- -->

> Remember the difference between aggregation and inheritance here! An `Arena` has `Team` objects, it _does not inherit_ from `Team`, and `Team` _does not inherit_ from `Arena`

# Prompting for Ability information

Create this method that will allow users to create an ability for any hero:

Build the `create_ability` function for your Arena class

```python
  def create_ability(self):
    '''Prompt for Ability information.
      return Ability with values from user Input
    '''
    name = input("What is the ability name?  ")
    max_damage = input(
      "What is the max damage of the ability?  ")

    return Ability(name, max_damage)
```

# Prompting for Weapon information

You will do this one on your own. Create this method that will allow users to create a weapon for any hero:

Build the `create_weapon` function for your Arena class

**HINT:** If you get stuck, look back at how `create_ability` is implemented.

```python
  def create_weapon(self):
    '''Prompt user for Weapon information
        return Weapon with values from user input.
    '''
    # TODO: This method will allow a user to create a weapon.
    # Prompt the user for the necessary information to create a new weapon object.
    # return the new weapon object.
    pass
```

# Prompting for Armor information

You will do this one on your own. Create this method that will allow users to create armor for any hero:

Build the `create_armor` function for your Arena class

**HINT:** If you get stuck, look back at how `create_ability` is implemented.

```python
  def create_armor(self):
    '''Prompt user for Armor information
      return Armor with values from user input.
    '''
    # TODO:This method will allow a user to create a piece of armor.
    #  Prompt the user for the necessary information to create a new armor object.
    #  return the new armor object with values set by user.
      pass
```

# Create a Hero for your Arena

Create this method that will allow users to create heroes for their arena. One of our students, Tasfia Addirita, helped us out here by partially implementing this method. You'll need to fill in the rest:

Build the `create_hero` function for your Arena class

```py
  def create_hero(self):
    '''Prompt user for Hero information
      return Hero with values from user input.
    '''
    hero_name = input("Hero's name: ")
    hero = Hero(hero_name)
    add_item = None
    while add_item != "4":
      add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
      if add_item == "1":
        # TODO add an ability to the hero
        # HINT: First create the ability, then add it to the hero
      elif add_item == "2":
        # TODO add a weapon to the hero
        # HINT: First create the weapon, then add it to the hero
      elif add_item == "3":
        # TODO add an armor to the hero
        # HINT: First create the armor, then add it to the hero
    return hero
```

# Create Teams for your Arena

Build the `build_team_one` and `build_team_two` functions for your Arena class

```py
  # build_team_one is provided to you
  def build_team_one(self):
    '''Prompt the user to build team_one '''
    # This method should allow a user to create team one.
    # Prompt the user for the number of Heroes on team one
    # call self.create_hero() for every hero that the user wants to add to team one.
    # Add the created hero to team one.
    numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
    for i in range(numOfTeamMembers):
      hero = self.create_hero()
      self.team_one.add_hero(hero)

  # Now implement build_team_two
  #HINT: If you get stuck, look at how build_team_one is implemented
  def build_team_two(self):
    '''Prompt the user to build team_two'''
    # TODO: This method should allow a user to create team two.
    # This method should allow a user to create team two.
    # Prompt the user for the number of Heroes on team two
    # call self.create_hero() for every hero that the user wants to add to team two.
    # Add the created hero to team two.
    pass
```

# Arena Battle

Create this method that will allow teams to battle it out in your arena! Don't overthink this one, you've already written everything you need for it.

Build the `team_battle` function for your Arena class

**HINT:** Attack is a method of the Team class

```py
  def team_battle(self):
    '''Battle team_one and team_two together.'''
    # TODO: This method should battle the teams together.
    # Call the attack method that exists in your team objects
    # for that battle functionality.
    pass
```

# Get Battle Stats
You may want to get statistics on how your battle went. Let's build that out now!

Build the `show_stats` function for your Arena class. We've built it out for Team One, you'll need to build it for Team Two!

```py
  def show_stats(self):
    '''Prints team statistics to terminal.'''
    # TODO: This method should print out battle statistics
    # including each team's average kill/death ratio.
    # Required Stats:
    #     Show surviving heroes.
    #     Declare winning team
    #     Show both teams average kill/death ratio.
    # Some help on how to achieve these tasks:
    # TODO: for each team, loop through all of their heroes,
    # and use the is_alive() method to check for alive heroes,
    # printing their names and increasing the count if they're alive.
    #
    # TODO: based off of your count of alive heroes,
    # you can see which team has more alive heroes, and therefore,
    # declare which team is the winning team
    #
    # TODO for each team, calculate the total kills and deaths for each hero,
    # find the average kills and deaths by dividing the totals by the number of heroes.
    # finally, divide the average number of kills by the average number of deaths for each team

    print("\n")
    print(self.team_one.name + " statistics: ")
    self.team_one.stats()
    print("\n")
    print(self.team_two.name + " statistics: ")
    self.team_two.stats()
    print("\n")

    # This is how to calculate the average K/D for Team One
    team_kills = 0
    team_deaths = 0
    for hero in self.team_one.heroes:
        team_kills += hero.kills
        team_deaths += hero.deaths
    if team_deaths == 0:
        team_deaths = 1
    print(self.team_one.name + " average K/D was: " + str(team_kills/team_deaths))

    # TODO: Now display the average K/D for Team Two

    # Here is a way to list the heroes from Team One that survived
    for hero in self.team_one.heroes:
        if hero.deaths == 0:
            print("survived from " + self.team_one.name + ": " + hero.name)

    #TODO: Now list the heroes from Team Two that survived
```

<!-- -->

Here's a challenge. That `show_stats` function is pretty big. Break it up into smaller helper functions to make the function less bloated and practice good code quality.

# Testing Arena

Test your functions by either creating a new test file and using pytest, or by calling your methods this way:

```python
if __name__ == "__main__":
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
```

# Feedback and Review - 2 minutes

**We promise this won't take longer than 2 minutes!**

Please take a moment to rate your understanding of the learning outcomes from this tutorial, and how we can improve it via our [tutorial feedback form](https://forms.gle/HLW9m4pSohADjkX1A)

This allows us to get feedback on how well the students are grasping the learning outcomes, and tells us where we can improve the tutorial experience.

# Creating a Game Loop

Our program right now has the parts and pieces to run once before it exits. This is fine for one off scripts that can run without user input, but games should be interactive. Our interactivity will come from a useful programming pattern called the **game loop**.

A typical game loop will do a few things over and over again:

* check for user input
* check length of time between loops
* update the game state
* render output to screen

Our terminal game isn't really your typical game so our game loop will be a bit different.

Since our game doesn't rely on quickly rendering complicated scenes to the screen we're not so concerned with frame rate and by extension the time between calling our render function. Our program instead will pause for user input and take actions depending on that.

You can create a simple game loop in your `arena.py` file this way:

This code snippet will get you started with your game loop. Here on every loop we battle our teams, show the battle outcome, and check whether we want to loop again.

```python
if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
```

**Congrats on finishing the Superhero Team Dueler tutorial!!** This is just the start of what you can make. Add to your game with these stretch challenges.

## Stretch Challenges

* Add a command line interface that allows for recreating or editing  of teams.
* Allow use of only "authorized" abilites, weapons, and armor controlled by the Arena.
* Add tests that cover more edge cases.
* Change the way health is dealt out across the team. i.e. create heroes that may take damage first or may take more of the team's damage.
* Write additional classes that implement different ways to attack or defend -- i.e. create a relic class that only defends against abilities.
* Develop a way to steal weapons and abilities from the opposing team.
* Add rewards for team success such as weapon drops.

# Commit

Commit your changes to GitHub. Feel free to use a custom message of your own, as long as it accuratley describes what you did.

```bash
$ git add . && git commit -m "Added battle arena" && git push
```