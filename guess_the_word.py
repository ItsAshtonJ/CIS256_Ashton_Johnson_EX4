#Ashton Johnson
#CIS256 Spring 2026
#Exercise Assignment 4

# Part 2: Writing the Game

import random

answer_list_computers = [
    "python", "computer", "software", "database", "programming", "internet", "github", "function", 
    "variable", "debugging", "coding", "systems", "keyboard", "monitor", "browser", "firewall", 
    "processor", "motherboard", "scanner", "printer", "framework", "pixel", "proxy", "bug", "node",
    "array", "backup", "byte", "cloud", "configure", "development", "hyperlink", "queue", "runtime"
]

answer_list_creatures = [
    "python", "tadpole", "zebra", "rhinoceros", "rattlesnake", "roadrunner", "quail", "horse", 
    "starfish", "honeybee", "butterfly", "kangaroo", "bison", "porcupine", "sloth", "ostrich", 
    "lobster", "ant", "grasshopper", "worm", "octopus", "hawk", "macaw", "turkey", "tarantula",
    "newt", "albatross", "pheasant", "shrimp", "fly", "grizzly", "mink", "chameleon", "boa"
]

def select_category():
    #Gives option to choose category
    print("\nChoose your word category")
    print("1. Computer & Programming Terms")
    print("2. Creatures & Animals")

    while True:
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            return answer_list_computers
        elif choice == "2":
            return answer_list_creatures
        else:
            print("Please choose value of 1 or 2")

def select_random_word(word_list):
    # Selects a random word from the chosen category 
    return random.choice(word_list).lower()

def display_word(word, guessed_letters):
    # Displays the word and keeps track of letters guessed
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def valid_guess(user_guess ,guessed_letters):
    # Tests to see if guess is valid for length, letter, and lowercase
    return (len(user_guess) == 1 and
            user_guess.isalpha() and
            user_guess.lower() not in guessed_letters)

def process_guesses(word, user_guess, guessed_letters):
    user_guess = user_guess.lower()
    guessed_letters.add(user_guess)

    if user_guess in word:
        letter_position = [i for i, letter in enumerate(word) if letter == user_guess]
        return {
            'correct': True,
            'positions': letter_position,
            'display': display_word(word, guessed_letters)
        }  
    else:
        return {
            'correct': False,
            'positions': [],
            'display': display_word(word, guessed_letters)
        }

def grab_guess(guessed_letters):
    while True:
        user_guess = input("\nGuess a letter: ").lower().strip()
        if valid_guess(user_guess, guessed_letters):
            return user_guess
        print("\ntry again, please enter a letter")

def play_hangman():
    word_list = select_category()
    word = select_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_guesses = 6

    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_guesses:
        print(f"Incorrect guesses left: {max_guesses - incorrect_guesses}")

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations the word was: {word}")
            return
        
        user_guess = grab_guess(guessed_letters)
        result = process_guesses(word, user_guess, guessed_letters)

        if result['correct']:
            print(f"'{user_guess}' is in the word")
        else:
            print(f"'{user_guess}' is NOT in the word")
            incorrect_guesses += 1
        
        print(result['display'])

    print(f"\nGame Over, the word was: {word}")

def main():
    while True:
        play_hangman()

if __name__ == "__main__":
    main()
 