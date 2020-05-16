"""
Program Name:           Lingo
Program Description:    This program emulates the hit game show "Lingo"
Author:                 AztecComputer
Date Created:           5/15/2020

Text File provided by https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
"""
import random
import sys


def check_endgame(word, guess, tries):
    if guess == word:
        replay = input(f"Congratulations, you've won! The word was: {word}. Play again? (y/n) ").lower()
    elif tries == 5:
        replay = input(f"I'm sorry, you lost. The word was: {word}. Play again? (y/n) ").lower()
    else:
        return 0
    if replay == "y":
        print("Starting new game...")
        main()
    else:
        print("Thanks for playing!!")
        sys.exit()


def get_word():
    word_file = open("sgb-words.txt", "r")
    text = word_file.read()
    text = text.split()
    num_words = len(text)
    return text[random.randint(0, num_words)]


def update_word(solution, indices): #  Updates displayed word containing correct indices
    word = ""
    for i in range(len(solution)):
        if i in indices:
            word += solution[i]
        else:
            word += "-"
    return word


def initialize_lingo_board():
    nums_found = False
    num_list = []
    board = []
    total_count = 0
    while not nums_found:
        if total_count == 25:
            nums_found = True
        else:
            num = random.randint(0, 100)
            if num not in num_list:
                num_list.append(num)
                total_count += 1
    for i in range(total_count):
        if not i % 5:
            board.append([])
            board[i // 5].append(num_list[i])
        else:
            board[i//5].append(num_list[i])
    return board


def display_board(board):  # Not currently implemented; displays bingo board
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end="\t")
        print()


def display_guesses(guesses):
    for guess in range(1, len(guesses)):
        display_word(guesses[guess])
        print()


def display_word(word):
    for letter in range(len(word)):
        print(f"{word[letter]}", end="\t")


def check_validity(guess, word):
    indices_correct = []
    if len(guess) != len(word):
        print("That's not a five letter word.")
        return indices_correct
    else:
        for letter in range(len(word)):
            if guess[letter] in word[0:] and guess[letter] == word[letter]:
                print(f"{guess[letter]} is in the right spot!")
                indices_correct.append(letter)
            elif guess[letter] in word[2:]:
                print(f"{guess[letter]} is a correct letter, but in the wrong spot!")
            else:
                print(f"{guess[letter]} is incorrect!")
    return indices_correct


def play_game(word, board):
    print(f"Welcome to Lingo.py. The object of this game is to guess a 5-letter word in 5 tries.")
    print(f"After each guess, you are told which letters are in the correct position, which aren't, and which are just wrong.")
    guess_allowance = 5
    tries = 0
    guess_so_far = word[0:2] + "---"
    tot_indices_correct = [0, 1]
    guesses = [word, guess_so_far]
    for i in range(guess_allowance):
        display_guesses(guesses)
        guess = input("\nHere's your word. Make a guess! ").lower()
        guesses[i+1] = guess
        cur_indices_correct = check_validity(guess, word)
        tot_indices_correct.extend(cur_indices_correct)
        guesses.append(update_word(word, tot_indices_correct))
        tries += 1
        check_endgame(word, guesses[i+1], tries)
        input("Press enter to continue...")


def main():
    word = get_word()
    board = initialize_lingo_board()
    play_game(word, board)
    return 0


main()
