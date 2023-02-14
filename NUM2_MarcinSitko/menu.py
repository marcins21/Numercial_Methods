import task2
import numpy as np
from matplotlib import pyplot as plt
import os


print("Marcin Sitko NUM2")
print("\n")
while True:
    print('''\n1) Pokaz Macierze\n2) Pokaz Obliczenia\n3) Dodatkowe \n\n4) Wyjscie''')

    user_input = int(input(": "))
    os.system('cls' if os.name == 'nt' else 'clear')
    if user_input == 1:
        for i in range(1,5):
            task2.print_matrix(i)
    elif user_input == 2:
        task2.show_results()
    elif user_input == 3:
        task2.additional()
    elif user_input == 4:
        break




