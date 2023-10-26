import random
class Armor:
    def __init__(self, name, max_block):
        '''instantiates the instance properties of:
        name: String
        max_block: integer'''

        self.name = name
        self.max_block = max_block

    def block(self):
        block_level = random.randint(0, self.max_block)
        return block_level
    
if __name__ == "__main__":
  # If you run this file from the terminal
  # this block is executed.
