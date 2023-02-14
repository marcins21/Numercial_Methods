import numpy as np
from matplotlib import pyplot as plt
from matplotlib.figure import  Figure

#Autor ---  Marcin Sitko
#ZADANIE NUM6 Podpunkt B)
#znalesc najwieksza co do modulu wartosc wlasna oraz odpowiadajacy jej wektor wlasny

def main(n):
    result_vectors = []
    iterations = []
    result_values = []


    A = np.array([[3, 4, 2, 4],
                  [4, 7, 1, -3],
                  [2, 1, 3, 2],
                  [4, -3, 2, 2]])

    u = np.array([[1], [1], [1], [1]])

    eigenvalue = 0
    for i in range(n):
        u = A @ u
        eigenvalue = abs(np.max(u))
        u = u / eigenvalue
        iterations.append(i)
        result_values.append(eigenvalue)
        result_vectors.append(u)


    result_vectors = np.reshape(result_vectors,(n,4))

    print('Najwieksza wartosc wlasna:', eigenvalue)
    print('Wektor wlasny\n', u)
    print("\n")

    # plt.yscale("log")

    plt.grid()
    plt.title("Maksymalna wartosc wlasna oraz wzgledem liczby iteracji")
    plt.ylabel("Najwieksza wartosc własna")
    plt.xlabel("Liczba Iteracji")
    #plt.plot(iterations,result_vectors,color="green")
    plt.plot(iterations,result_values,color="green")
    plt.show()


#main(100)

