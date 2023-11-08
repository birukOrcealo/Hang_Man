import random

class Hang_man:
    count = 0
    

    def __init__(self):
        self.word_list = ['Mango', 'Orange', 'Apple', 'Lemon']
        
        

    def random_word_generator(self):
        self.word = random.choice(self.word_list)
        self.list_ran_word = list(self.word)
        _ = '_'

        num_letters_to_reveal = 2
        positions_to_reveal = random.sample(range(len(self.word)), num_letters_to_reveal)
        self.chances = len(self.word) - num_letters_to_reveal

        display = [self.list_ran_word[i] if i in positions_to_reveal else _ for i in range(len(self.list_ran_word))]
        self.display = ' '.join(display)
        print(self.display)
        print(type(self.display))
    def validate_input(self):
        self.guess = input("Please enter a single letter: ")
        if len(self.guess) == 1 and self.guess.isalpha():
             print('Good guess')
        else:
                print("Oops! That is not valid input.")

    def update_display(self,display):
        self.display_list=list(self.display)
        for i in range(self.chances):
           guess = input("Please enter a letter: ")
           if '_' in self.display_list:  # Check if there are missing positions
              position = self.display_list.index('_')  # Find the first missing position
              self.display_list[position] = guess  # Fill in the missing position
              display=''.join(self.display_list)
              self.display_list=list(display)
              print(display)
              print(type(display))
           else:
            print("No more missing positions.")
        return display
    
    def compare(self,display):
       for i in range(len(self.word)):
            if display[i] == self.list_ran_word[i]:
               print("Correct letter found at position", i + 1, display[i])
            else:
              print("the correct letter is",self.list_ran_word[i])
    def play(self):
        self.random_word_generator()
        self.display_list = self.update_display(self.display)
        self.compare(self.display)

player = Hang_man()
player.play()


    
