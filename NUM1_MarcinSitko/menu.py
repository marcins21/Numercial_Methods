import task1
import os
print("\nMarcin Sitko 'NUM1'\n")
def menu():
    print("1) - Podpunkt A) dla FLOAT\n"
          "2) - Podpunkt A) dla DOUBLE\n\n"
          "3) - Podpunkt B) dla FLOAT\n"
          "4) - Podpunkt B) dla DOUBLE\n\n\n"
          "5) Eksperymentalna Funkcja exp(x) dla x=0.2\n"
          "6) Eksperymentalna Funkcja exp(x) dla x=5\n"
          "7) Eksperymentalna Funkcja exp(x) dla x=50")

def user_choice(graph_number):
    if graph_number == 1:
        task1.a_floatPrecision()

    if graph_number == 2:
        task1.a_doublePrecision()

    if graph_number == 3:
        task1.b_floatPrecision()

    if graph_number == 4:
        task1.b_doublePrecision()
    if graph_number == 5:
        task1.experimental()
    if graph_number == 6:
        task1.experimental1()
    if graph_number == 7:
        task1.experimental2()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    menu()
    user_input = int(input(": "))
    user_choice(user_input)
    clear_screen()








