import random
import string

WORDLIST_FILENAME = "words.txt"
alphabet = "abcdefghijklmnopqrstuvwxyz"
letterList = list(alphabet)
vowelLetters = "aeiou"


def load_words():

    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):

    return random.choice(wordlist)


wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):

    isGuessed = False
    for i in secret_word:
        if i in letters_guessed:
            isGuessed = True
        else:
            isGuessed = False
            break
    return isGuessed


def get_guessed_word(secret_word, letters_guessed):

    guessed_word = ''
    for i in secret_word:
        if i in letters_guessed:
            guessed_word += i+" "
        else:
            guessed_word += ' _ '
    return guessed_word



def get_available_letters(letters_guessed):

    available = ""
    for i in letters_guessed:
        if i in letterList:
            letterList.remove(i)

    for k in letterList:
        available += k
    return available

    
    

def hangman(secret_word):


    guesses = 6
    warnings = 3
    letters_guessed = list()

    print("Welcome to the game Hangman!\n")
    print("You have 6 guesses left, and 3 warnings\n"
          "You can only input an alphabet. If your input anything besides an alphabet, you lose 1 warning.\n"
          "If you have no remaining warnings, you lose 1 guess\n"
          "If your input a letter that hasn’t been guessed before and the letter is in the secret word, you lose no guesses.\n"
          "If your input a consonant that hasn’t been guessed and the consonant is not in the secret word, you loses 1 guess.\n"
          "If your input a vowel that hasn’t been guessed and the vowel is not in the secret word, you lose 2 guesses.\n")

    print("Let's start!\n"
          "I am thinking of a word that is ", len(secret_word), " letters long.")
    print("Avaliable letters: ", alphabet)

    while(guesses > 0):

        letter = input('\nPlease guess a letter: ')
        if not letter in alphabet:
            print("Please enter just available letters : ", alphabet)
            warnings -= 1
            if warnings < 0:
                guesses -= 1
                print("You have ", guesses, " guesses left")
            else:
                print("You have ", warnings, " warnings left")
        else:
            if letter in letters_guessed:
                print("You use this letter before!")
                warnings -= 1
                if warnings < 0:
                    guesses -= 1
                    print("You have no remaining warnings, so", guesses, " guesses left")
                else:
                    print("You have ", warnings, " warnings left")
            else:
                letters_guessed.append(letter)
                if letter in secret_word:
                    print("     Good guess: ", get_guessed_word(secret_word, letters_guessed))
                else:
                    print("     Opps! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
                    if letter in vowelLetters:
                        guesses -= 2
                    else:
                        guesses -= 1

                if is_word_guessed(secret_word, letters_guessed):
                    print("*************YOU WİN!!!**************")
                    break

                print("\nYou have ", guesses, " guesses left")
                print("Avaliable letters : ", get_available_letters(letters_guessed))

    if not is_word_guessed(secret_word, letters_guessed):
        print("***********YOU LOSE!!!!*************")
        print("the word : ", secret_word)



if __name__ == "__main__":
    

    secret_word = choose_word(wordlist)
    # secret_word = "antreman"
    hangman(secret_word)

