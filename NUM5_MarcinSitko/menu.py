import main
import os


def main_run():
    print("Marcin Sitko NUM5")
    print("\n")
    while True:
        print('''\n1) Pokazy Wyniki \n2) Pokaz Wykres\n3) Wieksza ilosc punktow startowych\n4) Pokaz roznice w wynikach z biblioteka numeryczna\n5) Wyjscie ''')

        user_input = int(input(": "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if user_input == 1:
            main.main()
        elif user_input == 2:
            main.grap(1)
        elif user_input == 3:
            main.user_choice()
        elif user_input == 4:
            main.roznice()
        elif user_input == 5:
            break
        else:
            break




main_run()
