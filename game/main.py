
class WordGuess:
    
    def __init__(self,word_list_file):
        self.word_list_file = word_list_file
        self.words = {}
    
	# takes user name as input and greets user
    def greetings(self):
        name = str(input("Enter your name : "))
        welcome = "{}, welcome to Word Guess Game!".format(name)
        print(welcome)
        
    # loads self.words dictionary and returns words_list 
    def loadWordList(self):
        with open(self.word_list_file, "r") as file:
            content = file.read().splitlines()
        
        for line in content:
            word, part_speech = line.split("-")
            self.words[word] = part_speech
    
        words_list = list(self.words.keys())
        return words_list
    
    # randomly chooses word from words_list and returns it 
    def wordToGuess(self):
        from random import choice
        
        word_to_guess = choice(self.loadWordList())
        return word_to_guess
    
    # gives hints to user
    def hintsForUser(self,word_to_guess):
        import time
        
        self.word_to_guess = word_to_guess 
        
        word_length = len(word_to_guess)
        first_char = word_to_guess[:2]
        last_char = word_to_guess[-2:]
        part_speech = self.words[word_to_guess]
        
        hints = [[word_length, first_char, last_char, part_speech],
             ["Word's length","First two letters","Last two letters","Parts of speech"]]
    
        total_hints = len(hints[0])    
    
        print("Hints for you: ")
        print("-" * 7)
        for i in range(total_hints):
            print("{} --> {}".format(hints[1][i],hints[0][i]))
            print()
            time.sleep(2)
	
        
    # takes user input and checks if it matches with word_to_guess

    @property   
    def userInput(self):
        word_to_guess = self.wordToGuess()
    
        self.greetings()
        self.hintsForUser(word_to_guess)
        
        user_input = str(input("Guess the word : "))
        if user_input == word_to_guess:
            print("Yes, your guess is right. \nThe word was, {}.".format(word_to_guess))
        else:
            print("Sorry, your guess is wrong. \nThe word was, {}.".format(word_to_guess))
        
    
        

# initializes the game with given file 
wordGuessGame = WordGuess("word-list.txt")

# starts the game
wordGuessGame.userInput
        
    
