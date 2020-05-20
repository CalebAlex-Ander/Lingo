"""
Program Name:           Lingo
Program Description:    This program emulates the hit game show "Lingo"
Author:                 AztecComputer
Date Created:           5/15/2020

Text File provided by https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
"""
import random
import sys


def check_if_right(word, guess, tries):
    if guess == word:
        print(f"Congratulations, you've won! The word was: {word}.")
        input("Press enter to continue...")
        return 1
    elif tries == 5:
        print(f"I'm sorry, you lost. The word was: {word}.")
        input("Press enter to continue...")
        return 0
    else:
        return 0


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


def initialize_lingo_board():  # Not currently implemented; initializes bingo board
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
        print(f"Guess {guess}: ", end=" ")
        display_word(guesses[guess])
        print()


def display_word(word):
    for letter in range(len(word)):
        print(f"\t{word[letter]}", end="\t")


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


def initialize_scores(players):
    scores = []
    for i in range(len(players)):
        scores.append(0)
    return scores


def initialize_players():
    num_players = int(input("How many players will there be? "))
    players = []
    for player in range(num_players):
        players.append(input(f"Please give a nickname for player {player + 1}: "))
    return players


def show_scoreboard(players, scores):
    print("Current Standings:")
    for i in range(len(players)):
        print(f"{players[i]}: {scores[i]}")
    print()


def play_game():

    board = initialize_lingo_board()
    players = initialize_players()
    scoreboard = initialize_scores(players)
    player_up = 0
    winning_score = 1

    while True:
        word = get_word()
        show_scoreboard(players, scoreboard)
        print(f"Okay {players[player_up]}, it's your turn!")
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
            if check_if_right(word, guesses[i+1], tries):
                scoreboard[player_up] += 1
                break
        if winning_score in scoreboard:
            print(f"Congratulations, {players[scoreboard.index(winning_score)]}, you've won!")
            sys.exit()
        else:
            player_up += 1
            if player_up == len(players):
                player_up = 0


def main():
    print(f"Welcome to Lingo.py. The object of this game is to guess a 5-letter word in 5 tries.")
    print(f"After each guess, you are told which letters are in the correct position, which aren't, and which are just wrong.")
    play_game()
    return 0


main()
