class Phrase:
    def __init__(self,phrase):
        self.phrase = phrase.lower()
    
    def __iter__(self):
        yield from self.phrase
        
    def __eq__(self,other):
        return self.phrase == other.phrase
            
    
    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter}', end = "")
            else:
                print("_ ", end = "")
                
    def check_guess(self,user_guess):
        if user_guess.lower() in self.phrase:
            return True
        
    
    def check_win(self,guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
    
    
        
                
    
                
                
        
            
        
