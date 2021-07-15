# @author: Sand1
# Hangman game


# -----------------------------------

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, "r")
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")

    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    return random.choice(wordlist)


# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """

    return not bool(
        {False for c in secretWord if c not in lettersGuessed}
    )  # bool({False}) is True


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """

    return " ".join([c if c in lettersGuessed else "_" for c in secretWord])


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """

    return "".join([c for c in "abcdefghijklmnopqrstuvwxyz" if c not in lettersGuessed])


def hangman(secretWord):
    """
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, lets the user know how many
      letters the secretWord contains.

    * Asks the user to supply one guess (i.e. letter) per round.

    * The user receives feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, also displays to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    """
    guesses = 8
    guesslist = []
    line = "--------------------------"

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long")

    while not isWordGuessed(secretWord, guesslist) and guesses:
        print(line)
        print("You have", guesses, "guesses left")
        print("Available letters:", getAvailableLetters(guesslist))

        letter = input("Please guess a letter: ").lower()

        if letter not in guesslist:
            guesslist.append(letter)
        else:
            print(
                "Oops! You've already guessed that letter:",
                getGuessedWord(secretWord, guesslist),
            )

            continue

        if letter in secretWord:
            print("Good guess:", getGuessedWord(secretWord, guesslist))
        else:
            print(
                "Oops! That letter is not in my word:",
                getGuessedWord(secretWord, guesslist),
            )
            guesses -= 1

    if guesses == 0:
        print(line)
        print("Sorry, you ran out of guesses. The word was", secretWord + ".")
    else:
        print(line)
        print("Congratulations, you won!")


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
