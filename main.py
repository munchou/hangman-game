import json
import random
import os
import lang_views


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def title():
    print("\n\t██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗")
    print("\t██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║")
    print("\t███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║")
    print("\t██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║")
    print("\t██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║")
    print("\t╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")
    print("\t                                              by munchou ©2023\n")


def language_select():
    while True:
        title()
        available_choice = ["1", "2"]
        print("\n\t1. ENGLISH")
        print("\t2. FRANCAIS")
        choice = input("\t-----> ")

        if choice not in available_choice:
            clear_screen()
            continue
        else:
            if choice == "1":
                language = "english"
                lang_view = lang_views.English
            elif choice == "2":
                language = "francais"
                lang_view = lang_views.Francais
            return language, lang_view


language, lang_view = language_select()


def loadWords(language):
    with open("words.json", encoding="utf8") as file:
        return json.load(file)[language]


def littleguy(health_start, health):
    lang_view.health(health, health_start)
    drawing = ["______", "|", "|", "|", "|", "|", "========"]

    if health <= 6:
        drawing[1] = "|    |"
    if health <= 5:
        drawing[2] = "|    @"
    if health <= 4:
        drawing[3] = "|    |"
    if health <= 3:
        drawing[3] = "|   /|"
    if health <= 2:
        drawing[3] = r"|   /|\ "
    if health <= 1:
        drawing[4] = "|   /"
    if health == 0:
        drawing[4] = r"|   / \ "

    for pic in drawing:
        print(f"\t{pic}")


def game():
    words = loadWords(language)
    # print(words)
    full_word = words[random.randrange(len(words))]
    for u in full_word:
        chosen_word = u
        chosen_word_def = full_word[u]

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    wrong_letters = []
    right_letters = []
    health = 7
    health_start = health
    victory = False
    moves = 0

    while True:
        clear_screen()
        title()

        lang_view.wrong_letters_list(wrong_letters)
        lang_view.right_letters_list(right_letters)

        result = ""
        if health == 0:
            break

        littleguy(health_start, health)

        for c in chosen_word:
            if c in right_letters:
                result += f"{c} "
            else:
                result += "_ "
        print(f"\t{result}")

        for c in chosen_word:
            if c not in right_letters:
                victory = False
                break
            else:
                victory = True

        if victory:
            break

        while True:
            letter_input = lang_view.letter_input()
            if letter_input in alphabet and len(letter_input) == 1:
                break
            elif letter_input == "EXIT":
                exit()
            else:
                lang_view.bad_input()
                continue

        if letter_input in chosen_word and letter_input not in right_letters:
            right_letters.append(letter_input)
            moves += 1
        elif letter_input not in chosen_word and letter_input not in wrong_letters:
            wrong_letters.append(letter_input)
            health -= 1
            moves += 1

        print(f'\t{"_ " * len(chosen_word)}')

    if victory:
        lang_view.victory(chosen_word_def)
    elif health == 0:
        littleguy(health_start, health)
        lang_view.defeat(chosen_word, chosen_word_def)

    lang_view.player_moves(moves)

    min_moves = ""
    for c in chosen_word:
        if c not in min_moves:
            min_moves += c

    lang_view.min_moves(min_moves)

    play_again = lang_view.play_again()
    if play_again == "y":
        game()
    else:
        exit()


game()
