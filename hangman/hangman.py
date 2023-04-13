import random
import string
from words import words 


def get_vaild_words(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()
 
def hangman():
    word = get_vaild_words(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    
    #user input
    while len(word_letters) > 0 and lives > 0:
        
        #used letter 
        print("you have ", lives, "You have used these letters: ", " " .join(used_letters))
        
        #what current word is
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word ", " " .join(word_list))
        
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 #take a life
                print("Letter is not in word")
        elif user_letter in used_letters:
            print("Sorry, you already guessed the word. Please try again. ")
        else:
            print("You typed the wrong character, please try again. ")
    if lives == 0:
        print("You died, sorry. The word was", word)
    else:
        print("yayy you guessed the word ", word, "!!")    
hangman()