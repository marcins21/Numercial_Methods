import os
import zada
import zadb


def main():
    print("Marcin Sitko NUM8")

    while True:
        print('''\n1) Podpunkt A\n2) Podpunkt B\n\n3) Wyjscie''')

        user_input = int(input(": "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if user_input == 1:
            zada.main()
        elif user_input == 2:
            zadb.main()
        elif user_input == 3:
            break

main()
