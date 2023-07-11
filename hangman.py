# assignment: Programming Assignment 1
# author: Samarth Ramesh
# date: 1/23/23
# file: hangman.py is a program that (put the description of the program)
# input: dictionaries, files, exceptions, loops, elif statements, functions, and string methods
# output: characters, statements

import random

dictionary_file = "dictionary.txt"


# import dictionary/read text file lines
def import_dictionary(filename):
    dictionary = {}
    if filename == filename:
        try:
            f = open(filename, "r")
            text = f.readlines()
            count = 0
            # remove the newline character
            for word in text:
                word = word.replace("\n", "")
                text[count] = word
                count += 1
            # update the length of all words 12 or greater to just 12
            for word in text:
                if len(word) >= 12:
                    dictionary.update({word: 12})
                elif len(word) > 1 and len(word) < 12:
                    dictionary.update({word: len(word)})
            f.close()
        # in case the file does not exist in the directory
        except IOError:
            print("The selected file cannot be open for reading!")
    return dictionary


# returns the word size and number of lives
def get_game_options():
    global lives
    global size
    list_length = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    lives_length = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    try:
        size = int(input("Please choose a size of a word to be guessed [3-12, default any size]:"))
        if size in list_length:
            get_key(size, dictionary)
            print("The word size is set to " + str(size) + ".")
        else:
            size = random.choice(list_length)
            get_key(size, dictionary)
            print("A dictionary word of any size will be chosen.")
    except ValueError:
        size = random.choice(list_length)
        get_key(size, dictionary)
        print("A dictionary word of any size will be chosen.")
    try:
        lives = int(input("Please choose a number of lives [1 – 10, default 5]:"))
        if lives in lives_length:
            print("You have " + str(lives) + " lives.")
        else:
            lives = 5
            print("You have " + str(lives) + " lives.")
    except ValueError:
        lives = 5
        print("You have " + str(lives) + " lives.")
    return (lives, size)


# creates a list of all the words in the dictionary with the selected word length
def get_key(size, dictionary):
    global list1
    list1 = []
    for key in dictionary:
        if dictionary[key] == size:
            list1.append(key)
    return list1


# creates a list of the displayed lives tracker
def game_lives(lives):
    global list_lives
    count = 0
    list_lives = []
    while count < lives:
        list_lives += "O"
        count += 1
    return (list_lives)


# creates a list of the displayed primary 'hangman' feature (accounts for hyphen in word)
def game_size(size):
    global list_size
    count = 0
    list_size = []
    if "-" in game_word:
        hyphen_index = game_word.index("-")
        while count < size:
            list_size.append("__")
            count += 1
        list_size[hyphen_index] = "-"
    else:
        while count < size:
            list_size.append("__")
            count += 1
    return (list_size)


# creates a string of the letter tracker
def game_chosen():
    global str_chosen
    str_chosen = str_chosen + chosen_letter + ", "
    return (str_chosen)


# MAIN
if __name__ == '__main__':

    # imports dictionary
    dictionary = import_dictionary(dictionary_file)

    print("Welcome to the Hangman Game!")
    # Print title
    # Main while loop
    while True:
        # calls the game options function
        get_game_options()

        # creates the game word
        game_word = random.choice(list1)
        game_word = game_word.upper()

        # initializes main variables/list
        size = len(game_word)
        chosen_letter = ""
        str_lives = " ".join(game_lives(lives))
        str_size = " ".join(game_size(size))
        str_chosen = "Letters chosen:\t"
        word_list = []
        # creates the word list
        for letter in game_word:
            word_list.append(letter)

        # inner game loop: runs while the lives are > 0 and there are still underscores in the hangman display
        while lives > 0 and "__" in list_size:

            # creating the display from the list in the corresponding functions
            str_lives = " ".join(list_lives)
            str_size = " ".join(list_size)

            # The ongoing print statement which is updated every iteration
            print(str_chosen + "\n" + str_size + " lives: " + str(lives), str_lives)

            # user letter input
            chosen_letter = input("Please choose a new letter >").upper()

            # algorithm for whether letter is correct or not
            if chosen_letter in str_chosen:
                print("You already chose this letter.")
            elif chosen_letter in game_word:
                print("You guessed right!")
                game_chosen()
                for letter in game_word:
                    word_list.append(letter)
                for letter in game_word:
                    if chosen_letter == letter:
                        word_index = word_list.index(chosen_letter)
                        word_list[word_index] = ""
                        list_size[word_index] = chosen_letter
            else:
                game_chosen()
                print("You guessed wrong, you lost one life.")
                lives_index = list_lives.index("O")
                list_lives[lives_index] = "X"
                lives -= 1
        # action for when the lives hit 0/restarts loop if user wishes to otherwise terminates the program
        if lives == 0:
            str_lives = " ".join(list_lives)
            str_size = " ".join(list_size)
            print(str_chosen + "\n" + str_size + " lives: " + str(lives), str_lives)
            print("You lost! The word is " + game_word + "!")
            restart = input("Would you like to play again [Y/N]?").upper()
            if restart == "N":
                print("Goodbye!")
                quit()
        # action for when the user wins/restarts loop if user wishes to otherwise terminates the program
        elif "__" not in list_size:
            str_lives = " ".join(list_lives)
            str_size = " ".join(list_size)
            print(str_chosen + "\n" + str_size + " lives: " + str(lives), str_lives)
            print("Congratulations!!! You won! The word is " + game_word + "!")
            restart = input("Would you like to play again [Y/N]?").upper()
            if restart == "N":
                print("Goodbye!")
                quit()