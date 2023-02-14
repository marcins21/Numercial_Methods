import zad6b
import zad6a
import os


def menu():
    print("1) Podpunkt A")
    print("2) Podpunkt B")
    print("3) Wyjscie")
print("Zadanie Numeryczne NUM6 Marcin Sitko")


while True:
    menu()

    user_input = int(input(":"))
    os.system('cls' if os.name == 'nt' else 'clear')
    if user_input == 1:
        user_operations_input = int(input("Podaj Ilosc iteracji ( wystarcza ok. 180 ): "))
        zad6a.main(user_operations_input)

    elif user_input == 2:
        user_operations_input = int(input("Podaj Ilosc iteracji ( wystarcza ok. 25 ): "))
        zad6b.main(user_operations_input)

    if user_input == 3:
        print("bye bye!")
        break
