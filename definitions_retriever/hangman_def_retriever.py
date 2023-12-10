import requests
import time
from bs4 import BeautifulSoup
import json


words_file = "downloaded_definitions.json"
site_url = "https://dictionary.cambridge.org/us/dictionary/english/"
allowed_char = "abcdefghijklmnopqrstuvwxyz- "

with open(words_file, encoding="utf8") as file:
    current_definitons = json.load(file)


def menu():
    while True:
        print("What would you like to do?")
        print('1. Import "words_to_import.txt" to download words from it')
        print("2. Manually add words to download")
        print("3. Peace in the World")
        print("4. Quit the program")
        choice = input("Your choice: ")
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("\n\tWRONG INPUT, TRY AGAIN.\n")


def words_from_file():
    input_file = open("words_to_import.txt", "r")
    content = input_file.read()
    return content.splitlines()


def add_words_manually():
    add_word = True
    words_to_download = []
    while add_word:
        word_to_dl = input(
            "Please enter the word you would like to get the definition for: "
        ).casefold()
        input_ok = True
        for character in word_to_dl:
            if character not in allowed_char:
                input_ok = False
                break
        if not input_ok:
            print(
                'Only alphabetical characters, space and "-" allowed, please try again.'
            )
            continue
        words_to_download.append(word_to_dl)
        print(f'"{word_to_dl} was added to the list of words to be retrieved."')
        while True:
            add_word_input = input("Add another word? (y/n) ").casefold()
            if add_word_input == "y":
                break
            elif add_word_input == "n":
                add_word = False
                break
        return words_to_download


def add_word_to_file(current_definitons, word_to_dl, new_def):
    current_definitons[word_to_dl] = new_def
    with open(words_file, "w", encoding="utf8") as json_file:
        """Write the new data to the file"""
        json.dump(current_definitons, json_file, ensure_ascii=False)


def download_words(site_url, words_to_download):
    for word_to_dl in words_to_download:
        url = f"{site_url}{word_to_dl}/"
        headers = {"User-Agent": "Mozilla/5.0"}
        req = requests.get(url, headers=headers)
        # print(req.status_code)
        if req.status_code == 404:
            print("# " * 20)
            print("Page not found, stopping the program.")
            print("# " * 20)
            exit()
        print(f"Current page: {url}")
        if req.ok:
            page_soup = BeautifulSoup(req.text, "html.parser")
            found_def = page_soup.find_all("div", {"class": "def ddef_d db"})

        if found_def:
            new_def = found_def[0].text.strip().capitalize()
            if new_def[-1] == ":":
                new_def = new_def.replace(new_def[-1], ".")
            else:
                new_def += "."
            print(new_def)
            add_word_to_file(current_definitons, word_to_dl, new_def)
            print(f'"{word_to_dl}" was successfully added.')
            # print("Waiting 5 seconds before next download")
            # time.sleep(5)
        else:
            print(f'"{word_to_dl}" not found, skipping')


choice = menu()
if choice == "1":
    print('Importing "words_to_import.txt".')
    words_to_download = words_from_file()
    download_words(site_url, words_to_download)


if choice == "2":
    print("Add manually words.")
    words_to_download = add_words_manually()
    download_words(site_url, words_to_download)


if choice == "3":
    print("Yes, well, no can do... :(")
    time.sleep(3)
    print("One of my greatest wishes.")
    time.sleep(2)
    print("残念だけどぉぉぉ。。。")
    time.sleep(4)
    print("申し訳ございませんね。")
    time.sleep(4)
    print("Bye now.")
    time.sleep(6)
    print("Still here?")
    time.sleep(1)
    print("Come on...")
    time.sleep(2)
    print("I'm going to close myself.")
    time.sleep(1)
    print("In 3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("Ploup!")
    time.sleep(1)
    exit()

if choice == "4":
    exit()
