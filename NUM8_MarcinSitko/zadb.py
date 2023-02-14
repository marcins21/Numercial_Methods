import numpy as np
import math
from matplotlib import pyplot as plt


def main():
    yi = []
    xi = np.linspace(1, 17, 100)
    A = []

    a = 0.3
    b = 5
    c = 2

    def a_matrix_composition(xi):
        for i in xi:
            A.append([math.pow(np.log(2*i),3),np.sin(i),math.pow(i,0.5)])
    a_matrix_composition(xi)

    def values(xi):
        for i in xi:
            yi.append( (a* math.pow(np.log(2*i),3)) + (b * np.sin(i))  + (c * math.pow(i,0.5)))
    values(xi)

    # Dodajemy szum
    noise = np.random.normal(0,2.8,300)
    def gaussianNoise(yi):
        noisedyi = []
        for i in range(len(yi)):
            noisedyi.append(yi[i]+noise[i])
        return noisedyi

    yi = gaussianNoise(yi)

    firstTerm = np.transpose(A) @  A
    secondTerm = np.transpose(A) @ yi

    result = np.linalg.solve(firstTerm,secondTerm)
    print("\nWEKTOR WSPOLCZYNNIKOW\n",result)

    print("\n\nMACIERZ A\n")
    print(A)

    print("\n\nWektor wartsoci X\n")
    print(xi)
    print("\n\nWektor wartosci Y\n")
    print(yi)


    resultFunction = []
    xs = []
    for i in xi:
        xs.append(i)
        FX = (result[0]* math.pow(np.log(2*i),3)) + (result[1] * np.sin(i))  + (result[2] * math.pow(i,0.5))
        resultFunction.append(FX)

    plt.plot(xs,resultFunction)
    plt.title("Aproksymacja Funkcji na podstawie punktow")
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.savefig("aprox.svg")
    plt.show()

    plt.scatter(xi,yi)
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.title("Szum")
    plt.savefig("szum.svg")
    plt.show()

#main()