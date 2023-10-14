import json


words_file = "words.json"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def title():
    print("\n\t██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗")
    print("\t██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║")
    print("\t███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║")
    print("\t██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║")
    print("\t██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║")
    print("\t╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝")
    print("\tWORDS FILE EDITOR                             by munchou ©2023\n")


def language_select():
    title()
    while True:
        available_choice = ["1", "2", "123"]
        print("\n\t1. ENGLISH")
        print("\t2. FRANCAIS")
        print("\t123. EXIT")
        choice = input("\t-----> ")

        if choice not in available_choice:
            continue
        else:
            if choice == "1":
                language = "english"
            elif choice == "2":
                language = "francais"
            elif choice == "123":
                exit()
            return language


language = language_select()


def loadWords():
    with open(words_file, encoding="utf8") as file:
        return json.load(file)


words = loadWords()
# print(words)
words_list = words[language]
words_keys = []
for i in words_list:
    for u in i:
        words_keys.append(u)


def add_word_and_def():
    """Input for the new word and its definition.
    The program will check if the word already exists."""
    while True:
        while True:
            bad_char = False
            word = input("Word: ").upper()
            if word in words_keys:
                print(f"{word} has already been added, please add a new word.")
                continue
            for character in word:
                if character not in alphabet:
                    bad_char = True
                    print("Invalid characters, please try again")
                    break
            if bad_char:
                continue
            break

        definition = input("Definition: ")
        print("You added:")
        print(f"\t{word}: {definition}")
        confirm = input("Do you confirm that choice (y/n): ").casefold()
        if confirm == "y":
            break
        continue

    return {word: definition}


new_word = add_word_and_def()
words_list.append(new_word)

with open(words_file, "w", encoding="utf8") as json_file:
    """Write the new data to the file"""
    json.dump(words, json_file, ensure_ascii=False)
