import numpy as np
from matplotlib import pyplot as plt





def main():
    xi = []  # X
    yi = []  # Y
    A = []
    terms = []
    # wczytanie danych z pliku
    def readLinesFromFile(filename="data_NUM8.txt"):
        with open(filename) as file:
            for line in file.readlines():
                x,y = line.split(" ")
                xi.append(float(x))
                yi.append([float(y)])
    readLinesFromFile()

    def a_matrix_composition(xi:list):
        for i in xi:
            A.append([np.sin(2*i),np.sin(3*i),np.cos(5*i),np.exp(-1*i)])
    a_matrix_composition(xi)



    firstTerm = np.transpose(A) @  A
    secondTerm = np.transpose(A) @ yi

    result = np.linalg.solve(firstTerm,secondTerm)
    print("\nWEKTOR WSPOLCZYNNIKOW\n",result)

    print("\n\nMACIERZ A\n")
    for i in range(len(A)):
        for j in range(4):
            print(A[i][j],end=" ")
        print(" ")

    print("\n\nWektor wartsoci X\n")
    print(xi)
    print("\n\nWektor wartosci Y\n")
    print(yi)

    resultFunction = []
    xs = []
    for i in xi:
        xs.append(i)
        FX = (result[0][0]*np.sin(2*i))+(result[1][0]*np.sin(3*i)) + (result[2][0]* np.cos(5*i)) + (result[3][0]* np.exp(-1*i))
        resultFunction.append(FX)


    #print(resultFunction)

    plt.plot(xs,resultFunction)
    plt.xlabel("Oś X")
    plt.ylabel("Oś Y")
    plt.title("Aproksymacja Funkcji na podstawie podanych punktow")
    plt.grid()
    plt.savefig("result.svg")
    plt.show()


#main()










