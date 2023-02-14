from functools import reduce

import numpy as np
import matplotlib.pyplot as plt
import copy
import random


n = 100
iteracje = 175
precyzja = 10 ** (-15)

wektor_w_wolnych = list(range(1, n + 1))

norm_jacobii = []
norm_siedel = []


def get_matrix():
    macierz = random.sample(range(iteracje), 100)
    return macierz


#Zdefiniowanie macierzy n x n potrzebnej do uzysaknia wyniku z biblioteki numerycznej
def definingMatrix(n):
    #Diagonal
    diag = np.empty(n)
    diag.fill(3)

    # 1sub diagonal
    sub1diag = np.empty(n)
    sub1diag.fill(1)

    sub2diag = np.empty(n)
    sub2diag.fill(0.2)

    #1above diagonal
    abv1diag = np.empty(n)
    abv1diag.fill(1)

    #2above diagonal
    abv2diag = np.empty(n)
    abv2diag.fill(0.2)

    diag_rows = []
    diag_rows.append(sub1diag)
    diag_rows.append(diag)
    diag_rows.append(abv1diag)
    diag_rows.append(abv2diag)

    size = n
    vals = [sub2diag,sub1diag,diag, abv1diag, abv2diag]
    offset=-2
    res = reduce(lambda a, b: a+np.eye(n,k=b[0]+offset)*b[1], enumerate(vals), np.zeros((n, n)))
    return res



#Metoda Gaussa Seiddela
def gauss_siedel(macierz, iteracje):
    res = []
    norm1 = 0
    while iteracje:
        macierz_cp = macierz.copy()

        for i in range(n):

            #Wzor dla pierwszego wiersza macierzy
            if (i == 0):
                macierz[i] = (wektor_w_wolnych[i] - macierz[i + 1] - 0.2 * macierz[i + 2]) / 3

            #Wzor dla pierwszego wiersza nr1
            elif (i == 1):
                macierz[i] = (wektor_w_wolnych[i] - macierz_cp[i - 1] - macierz[i + 1] - 0.2 * macierz[i + 2]) / 3

            #Obsluga ostatnich n-1 wiersza macierzy
            elif (i == n - 1):
                macierz[i] = (wektor_w_wolnych[i] - macierz_cp[i - 1] - 0.2 * macierz_cp[i - 2]) / 3

            #Obsluga ostatniego wiersza macierzy
            elif (i == n - 2):
                macierz[i] = (wektor_w_wolnych[i] - macierz_cp[i - 1] - 0.2 * macierz_cp[i - 2] - macierz[i + 1]) / 3

            #Dla wszystkich innych przypadkow poza n-1, n-2, 0, 1
            else:
                macierz[i] = (wektor_w_wolnych[i] - macierz_cp[i - 1] - 0.2 * macierz_cp[i - 2] - macierz[i + 1] - 0.2 * macierz[i + 2]) / 3


        norm2 = np.sqrt(sum(map(lambda a, b: (a - b) ** 2, macierz, macierz_cp)))
        prec = abs(norm1 - norm2)

        norm_siedel.append(norm2)
        res.append(copy.deepcopy(macierz))

        #Sprawdzanie normy dla wyniku przyblizonego do ^-15
        if prec < precyzja:
            norm_siedel.append((prec))
            break
        norm1 = norm2

        #Iterator
        iteracje -= 1

    print("Jacobi:")
    for i in range(len(macierz)):
        if i % 20 == 0:
            print()
        print(macierz[i], end=" ")
    # print(macierz)
    print("\n")
    return res


#Metoda Jacobiego
def jacobi(macierz, iteracje):
    res = []
    norm1 = 0
    while iteracje:
        macierz_cp = macierz.copy()
        for i in range(n):
            #Wzor dla 0 wiersza macierzy
            if (i == 0):
                macierz[i] = (wektor_w_wolnych[i] - macierz[i + 1] - 0.2 * macierz[i + 2]) / 3

            #Wzor dla 1 wiersza macierzy
            elif (i == 1):
                macierz[i] = (wektor_w_wolnych[i] - macierz[i - 1] - macierz[i + 1] - 0.2 * macierz[i + 2]) / 3

            #Wzor dla n-1 wiersza macierzy
            elif (i == n - 1):
                macierz[i] = (wektor_w_wolnych[i] - macierz[i - 1] - 0.2 * macierz[i - 2]) / 3


            #Wzor dla ostatniego wiersza macierzy
            elif (i == n - 2):
                macierz[i] = (wektor_w_wolnych[i] - macierz[i - 1] - 0.2 *macierz[i - 2] - macierz[i + 1]) / 3

            #Wzor dla wszystkich pozostałych iteracji
            else:
                macierz[i] = (wektor_w_wolnych[i] - macierz[i - 1] - 0.2 * macierz[i - 2] - macierz[i + 1] - 0.2 * macierz[i + 2]) / 3

        #licze norme
        norm2 = np.sqrt(sum(map(lambda a, b: (a - b) ** 2, macierz,macierz_cp)))
        norm_jacobii.append(norm2)

        res.append(copy.deepcopy(macierz))

        #zaokreaglenie dla odpowiedniej precyzji e^-15
        if abs(norm1 - norm2) < precyzja:
            break
        norm1 = norm2
        iteracje -=  1

    print("Gauss-Seidel:")
    for i in range(len(macierz)):
        if i % 20 == 0:
            print()
        print(macierz[i],end=" ")
    #print(macierz)
    print("\n")
    return res


def right_solution():
    print("\n\n Rozwiazanie z bilioteki numerycznej \n\n ")
    A = definingMatrix(100)
    b = np.arange(1, 101).reshape(100, 1)
    solve = np.linalg.solve(A, b)
    for i in range(len(solve)):
        if i % 20 == 0:
            pass
            print()
        print(solve[i], end=" ")

    return np.array(solve)

def roznice():
    matrix = get_matrix()
    numerical = right_solution()
    result1 = np.array(jacobi(matrix.copy(), iteracje))
    result2 = gauss_siedel(matrix.copy(), iteracje)

    for i in range(len(result1[40])):
        roznica_res1.append(numerical[i] - result1[40][i])

    for i in range(len(result2[149])):
        roznica_res2.append(numerical[i] - result2[149][i])

    print("\nRoznice Gaus Siedel z bilioteka numeryczna")
    print("\n", roznica_res1)

    print("\nRoznice Jacobii Z bilbioteka numeryczna")
    print("\n",roznica_res2)

w1 = []
w2 = []
res1 = []
res2 = []
random_wektors = []
roznica_res2 = []
roznica_res1 = []

def main(plotting:bool=False):

    matrix = get_matrix()
    random_wektors.append(matrix)
    result1 = np.array(jacobi(matrix.copy(), iteracje))
    result2 = gauss_siedel(matrix.copy(), iteracje)
    numerical = right_solution()

    for i in range(len(result1)-1):
        res1.append(i)
    for j in range(len(result2)-1):
        res2.append(j)

    lastnumber1 = result1[-1]
    for i in range(len(result1) - 1):
        w1.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, result1[i], lastnumber1))))

    lastnumber2 = result2[-1]
    for i in range(len(result2) - 1):
        w2.append(np.sqrt(sum(map(lambda a, b: (a - b) ** 2, result2[i], lastnumber2))))


    if plotting:
        plt.plot(res1, w1)
        plt.plot(res2, w2)


def grap(n):
    for i in range(n):
        main(plotting=True)
    plt.grid()
    plt.yscale("log")
    plt.xlabel('Ilosc Iteracji')
    plt.ylabel("Blad")
    plt.legend(['Gaus-Seidel', 'Jacobi'])
    plt.title('Metoda Iteracyjna  x')
    plt.savefig('myfig.svg')
    plt.show()


def user_choice():
    user_input = int(input("Podaj ile losowych punktow startowych wybrac: "))
    grap(user_input)



# main(False)
# grap(1)
#user_choice()
