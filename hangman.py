# hangman game by Roya Pourajabian
import csv
import random


# a package that will help us to pick a random word of over list
def hangman():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wrong_guess = 0  #
    with open("secret_words.csv", "r") as f:
        reader = csv.reader(f)
        my_list = list(reader)  # convert the csv file into a list
        random_word = random.choice(my_list[0])  # use random package to choose a random word
        displayWord = []
        random_word = random_word.upper()
        for i in range(len(random_word)):
            displayWord.append("_")
        secret_word = ""
        for i in range(len(displayWord)):  # for display pretty the secret word like ----
            secret_word += displayWord[i]
        print(secret_word)
    gameOver = False  # to manage the game
    while gameOver is False:
        guess = input("please guess a letter: ").upper()
        if guess == random_word:
            print("you win")
            exit()
        if guess not in alphabet:
            print("You did enter a valid guess. Please try again.")
        if guess in random_word:  # replace the right alphabet with _
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    displayWord[i] = guess
                    secret_word = ""
                    for x in range(len(displayWord)):
                        secret_word += displayWord[x]
            print(secret_word)

        else:
            wrong_guess += 1
            print("wrong guess! try again.")
            if wrong_guess == 1:
                print("________      ")
                print("|      |      ")
                print("|             ")
                print("|             ")
                print("|             ")
                print("|             ")
            elif wrong_guess == 3:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|             ")
                print("|             ")
                print("|             ")
            elif wrong_guess == 5:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /       ")
                print("|             ")
                print("|             ")
            elif wrong_guess == 7:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|      ")
                print("|             ")
                print("|             ")
            elif wrong_guess == 9:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|             ")
                print("|             ")
            elif wrong_guess == 10:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|     /       ")
                print("|             ")
            print(secret_word)
            print(" grade:", 0 - wrong_guess)
            if wrong_guess == 11:
                print("________      ")
                print("|      |      ")
                print("|      0      ")
                print("|     /|\     ")
                print("|     / \     ")
                print("|             ")
                print("game over!")
                print("the word was : ", random_word)
                gameOver = True
        if "_" not in displayWord:
            print("you win")
            exit()


hangman()
