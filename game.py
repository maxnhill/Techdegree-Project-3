import random
import time
from phrase import Phrase


class Game:
    
    def __init__(self):
        self.missed = 0
        self.phrases = [Phrase("Holy Smokes"), Phrase("Your Mom"), Phrase("Thank God"), Phrase("I love New York"), Phrase("Jesus Loves you")]
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]
        self.hangman = " "
        self.hang = "O|--< "
        
    def get_random_phrase(self):
        the_phrase = random.choice(self.phrases)
        return(the_phrase)
    
    def welcome(self):
        print("=========================================")
        print("Welcome to the Hangman: Phrases Edition!")
        print("=========================================")
        time.sleep(2)
        print("=> Start by guessing a letter you think is in the phrase.")
        time.sleep(2)
        print("=> You get five chances to guess the phrase.")
        time.sleep(2)
        print("=> Good luck Mi Amigo!")
        time.sleep(1)
        
        
    def game_start(self):
        self.welcome()
        game = True
        while game:
            num_attempts = 5
            
            while True:
                time.sleep(1)
                print(f"Number missed: {self.missed} {self.hangman}")
                self.active_phrase.display(self.guesses)
                if self.missed >= num_attempts:
                    print("\nOh soryy! You've used up your number of attempts.")
                    break
                
                try:
                    user_guess = self.get_guess()
                    if len(user_guess) >=2 or user_guess.isnumeric() == True:
                        raise ValueError
                        
                except ValueError:
                    time.sleep(2)
                    print("\nPlease enter ONE alphabetical letter")
                    print("\n")
                    continue
                    
                self.guesses.append(user_guess)
                
                if user_guess not in self.active_phrase:
                    self.missed += 1
                    self.hangman += self.hang[0]
                    self.hang = self.hang[1: :]
                    
                    
                    
                elif self.active_phrase.check_win(self.guesses):
                    time.sleep(1)
                    print("\nYou guessed the phrase!")
                    break
                    
            time.sleep(1)        
            again = input("Do you want to play again? (Yes/No): ")
            if again.lower()== 'no':
                print("\nOK bye, thank you for playing my game!") 
                time.sleep(2)
                game= False
                
            elif again.lower()=='yes':
                time.sleep(2)
                print("\nLet's give it another go!")
                self.__init__()
                
        self.game_over()
            
                             
    def get_guess(self):
        return input("\nPlease choose a letter: ")
            
    
    def game_over(self):
        if self.active_phrase.check_win(self.guesses):
            print("Thank you for playing Hangman: Phrase Edition!")
            

            
            
        
        
        
    
 