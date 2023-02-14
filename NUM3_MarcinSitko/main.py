import testingField
import os


def main():
    print("Marcin Sitko NUM3")
    print("\n")
    while True:
        print('''\n1) Zadanie NUM3\n2) Sprawdz Poprawnosc Olbiczen\n3) Zadanie Dodatkowe\n4) Wyznacznik macierzy U \n\n5) Wyjscie''')

        user_input = int(input(": "))
        os.system('cls' if os.name == 'nt' else 'clear')
        if user_input == 1:
            testingField.main()
        elif user_input == 2:
            testingField.checkResults()
        elif user_input == 3:

            while True:
                print("1) Wykonaj Obliczenia Wystarczy Wykonac to 1 raz\n2) Pokaz Wykres ilustrujacy zaleznosc pomiedzy wielkoscią n (macierzy) a czasem wykonania algorytmu\n"
                      "3) Pokaz czasy Wykonania algorytmow\n4) Wyjscie")
                user_input_2 = int(input(": "))
                os.system('cls' if os.name == 'nt' else 'clear')

                if user_input_2 == 1:
                    print("\n")
                    testingField.compute()
                    print("\n")
                elif user_input_2 == 2:
                    testingField.graph()
                elif user_input_2 == 3:
                    testingField.showResultsMore()
                elif user_input_2 ==4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break

        elif user_input == 4:
            testingField.matrixDet()

        elif user_input == 5:
            break

main()
