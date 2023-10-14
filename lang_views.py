# HANGMAN languages: English, Francais


class English:
    def health(health, health_start):
        print(f"\tHEALTH: {'O '*health}{'X '*(health_start-health)}")

    def wrong_letters_list(wrong_letters):
        print(f"\n\tWRONG USED LETTERS: {wrong_letters}")

    def right_letters_list(right_letters):
        print(f"\tRIGHT USED LETTERS: {right_letters}")

    def letter_input():
        letter_input = input('\n\tEnter a letter ("exit" to quit): ')
        return letter_input.upper()

    def bad_input():
        print("\tPlease enter a letter that belongs to the alphabet.")

    def victory(chosen_word_def):
        print(f"\n\t{chosen_word_def}")
        print(
            "\n\tCONGRATULATIONS, YOU WON! THE LITTLE GUY DIDN'T GET HANGED. BUT WHAT IF HE REALLY WAS GUILTY...?"
        )

    def defeat(chosen_word, chosen_word_def):
        print(f"\n\tYOU LOST, THE RIGHT WORD WAS [{chosen_word}]")
        print(f"\n\t{chosen_word_def}")
        print("\n\tTHE LITTLE GUY GOT HANGED. LET'S HOPE HE WAS GUILTY...\n")

    def player_moves(moves):
        print(f"\n\tNumber of moves: {moves}")

    def min_moves(min_moves):
        print(f"\tNumber of minimum moves for that word: {len(min_moves)}")

    def play_again():
        while True:
            again = input("\n\tWould you like to play again (y/n)? ").casefold()
            if again == "y":
                return "y"
            elif again == "n":
                return "n"
            else:
                continue


class Francais:
    def health(health, health_start):
        print(f"\tVIE: {'O '*health}{'X '*(health_start-health)}")

    def wrong_letters_list(wrong_letters):
        print(f"\n\tMAUVAISES LETTRES ENTRÉES: {wrong_letters}")

    def right_letters_list(right_letters):
        print(f"\tLETTRES CORRECTES ENTRÉES: {right_letters}")

    def letter_input():
        letter_input = input('\n\tEntrez une lettre ("exit" pour quitter) : ')
        return letter_input.upper()

    def bad_input():
        print("\tVeuillez entrer une lettre de l'alphabet.")

    def victory(chosen_word_def):
        print(f"\n\t{chosen_word_def}")
        print(
            "\n\tFÉLICITATIONS, VOUS AVEZ GAGNÉ ! LE BONHOMME NE S'EST PAS FAIT PENDRE. ET SI IL ÉTAIT VRAIMENT COUPABLE...?"
        )

    def defeat(chosen_word, chosen_word_def):
        print(f"\n\tVOUS AVEZ PERDU, LE MOT A TROUVER ÉTAIT [{chosen_word}]")
        print(f"\n\t{chosen_word_def}")
        print(
            "\n\tLE BONHOMME S'EST FAIT PENDRE. EN ESPÉRANT QU'IL ÉTAIT COUPABLE...\n"
        )

    def player_moves(moves):
        print(f"\n\tNombre de coups: {moves}")

    def min_moves(min_moves):
        print(f"\tNombre minimum de coups pour ce mot : {len(min_moves)}")

    def play_again():
        while True:
            again = input("\n\tSouhaitez-vous rejouer (o/n)? ").casefold()
            if again == "o":
                return "y"
            elif again == "n":
                return "n"
            else:
                continue
