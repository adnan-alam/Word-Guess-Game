import random
import time


class WordGuess:
    def __init__(self,word_stock_file):
        self.word_stock_file = word_stock_file
        self.words = {}
   
    # takes user name as input and print greetings
    def get_greetings(self):
        name = str(input("Enter your name : ").strip())
        welcome = "{}, welcome to Word Guess Game!".format(name)
        print(welcome)
    
    # return word list consist of words and parts of speech from the given txt file	
    def get_word_list(self):
        with open(self.word_stock_file, "r") as file:
            content = file.read().splitlines()
        
        for line in content:
            word, parts_speech = line.split("-")
            self.words[word] = parts_speech
    
        words_list = list(self.words.keys())
        return words_list
    
    # returns a randomly choosen word from word list
    def get_word(self):
        word_to_guess = random.choice(self.get_word_list())
        return word_to_guess
    
    # gives hints to user about the word to be guessed	
    def get_hints(self,word_to_guess):
        self.word_to_guess = word_to_guess 
        word_length = len(word_to_guess)
        first_chars = word_to_guess[:2]
        last_chars = word_to_guess[-2:]
        parts_speech = self.words[word_to_guess]
        
        hints = [[word_length, first_chars, last_chars, parts_speech],
             ["Word's length", "First two letters", "Last two letters", "Parts of speech"]]
    
        total_hints = len(hints[0])    
    
        print("Hints for you: ")
        print("-" * 7)
        for i in range(total_hints):
            print("{} --> {}".format(hints[1][i],hints[0][i]))
            print()
            time.sleep(2)
        
    # checks user input with the word to be guessed and prints result
    @property   
    def start_game(self):
        word_to_guess = self.get_word()
        self.get_greetings()
        self.get_hints(word_to_guess)
        user_input = str(input("Guess the word : ").strip())
        if user_input.lower() == word_to_guess.lower():
            print("Yes, your guess is right. \nThe word was, {}.".format(word_to_guess))
        else:
            print("Sorry, your guess is wrong. \nThe word was, {}.".format(word_to_guess))
        
    
    
word_guess_game = WordGuess("word-list.txt")
word_guess_game.start_game
