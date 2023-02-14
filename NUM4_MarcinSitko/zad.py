from functools import reduce
import scipy.linalg as la
import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot as plt

def definingAforNumerical(n):
    # Diagonal
    diag = np.empty(n)
    diag.fill(9)
    # 1above diagonal
    abv1diag = np.empty(n)
    for i in range(1, len(abv1diag)):
        abv1diag[i] = 7

    diag_rows = []

    diag_rows.append(diag)
    diag_rows.append(abv1diag)

    size = n
    vals = [diag, abv1diag]

    offset =0
    res = reduce(lambda a, b: a + np.eye(n, k=b[0] + offset) * b[1], enumerate(vals), np.zeros((n, n)))
    return res

def definingA(n):
    A =[[],[]]
    for i in range(n):
        A[0].append(9)
    for j in range(n):
        A[1].append(7)
    A = np.array(A)
    return A

def definingU(n):
    U = []
    for i in range(n):
        U.append(1)
    U = np.array(U)
    return U.reshape(n,1)

def definingV(n):
    V = []
    for i in range(n):
        V.append(1)
    V = np.array(V)
    return  V.reshape(1,n)


def definingB(n):
    B = []
    for i in range(n):
        B.append(5)
    B = np.array(B)
    return B.reshape(n,1)


def numerical(n):

    print("Bilbioteka Numerczna: ",end="   ")
    t0 = timer()
    A = definingAforNumerical(n)
    u = definingU(n)
    v = definingV(n)
    b = definingB(n)
    Ahat = A + np.outer(u, b)
    LU, piv = la.lu_factor(A)

    def solveANumerical(b):
        return la.lu_solve((LU, piv), b)

    #print(la.norm(np.dot(A, solveANumerical(b)) - b))
    xhat = (np.linalg.inv(A + np.dot(u,v)) @ b)

    xhat2 = solveANumerical(b) - (solveANumerical(u) @ np.dot(v, solveANumerical(b))/(1+np.dot(v, solveANumerical(u))))

    t1 = timer()
    czas  = t1-t0

    print("Czas Policzenia ",czas)
    return xhat2



def ObliczZ(n):
    n =n-1
    z = np.zeros(n)
    z = list(z)
    z.insert(len(z),5/9)

    for i in range(0, n):
        x = (5 - (7 * z[n-i])) / 9
        z[n-i-1] = x

    z = np.array(z)
    return z.reshape(n+1,1)

def ObliczU(n):
    n=n-1
    u = np.zeros(n)
    u = list(u)
    u.insert(len(u),1/9)

    for i in range(0, n):
        x = (1 - (7 * u[n-i])) / 9
        u[n-i-1] = x

    u = np.array(u)
    return u.reshape(n + 1, 1)


def mojmorisson(n):
    #Macierz A
    print("Moj Morison ",end="   ")
    t0 = timer()
    A = definingA(n)
    #A = definingAforNumerical(50)
    u = definingU(n)
    v = definingV(n)
    b = definingB(n)

    z = ObliczZ(n)
    x = ObliczU(n)

    morrison = z - ((x @ np.dot(v,z))/(1+(np.dot(v,x))))
    t1 = timer()
    czas = t1-t0
    print("Czas Policzenia Morrsisona ",czas)
    return morrison

myresult = []
numerical_lib_result = []
graphList = []
def compute():
    print("\nRozwiazanie Rownanian macierzowych dla 100<n<5.000 z krokiem 600")

    print("\n Rozwiazywanie tych rownan moze zajac kilkanascie sekund prosze o cierpliwosc")

    for i in range(50,5000,600):
        print(i)
        graphList.append(i)
        #moj algorytm
        t0 = timer()
        mojmorisson(i)
        t1 = timer()
        moj_czas = t1 - t0
        myresult.append(moj_czas)

        t2 = timer()
        numerical(i)
        t3 = timer()
        numeryczny_czas = t3-t2
        numerical_lib_result.append(numeryczny_czas)

def showResults(n):
    A = definingA(n)
    # A = definingAforNumerical(50)
    u = definingU(n)
    v = definingV(n)
    b = definingB(n)

    z = ObliczZ(n)
    x = ObliczU(n)

    morrison = z - ((x * np.dot(v, z)) / (1 + (np.dot(v, x))))
    morrison = np.array(morrison)
    morrison  = morrison.reshape(1,n)
    print("Wynik mojego algorytmu morissona:" ,morrison)

    A = definingAforNumerical(n)
    u = definingU(n)
    v = definingV(n)
    b = definingB(n)
    Ahat = A + np.outer(u, b)
    LU, piv = la.lu_factor(A)

    def solveANumerical(b):
        return la.lu_solve((LU, piv), b)

    xhat2 = solveANumerical(b) - (
                solveANumerical(u) * np.dot(v, solveANumerical(b)) / (1 + np.dot(v, solveANumerical(u))))

    xhat2 = np.array(xhat2)
    xhat2 = xhat2.reshape(1,n)

    print("Wynik algorytmu numerycznego morissona: ",xhat2)

    sub  = xhat2 - morrison
    print("Roznica: ",sub)

#Funkcja Pokazujaca Graf, z czasem wykonania obliczen
def graph():
    plt.title("Zaleznosc czasu wykonania sie algorytmu od wielkosci macierzy ")
    plt.xlabel("Wielkosc Macierzy",)
    plt.ylabel("Czas Wykonania algorytmu (s)")
    plt.plot(graphList, myresult, label='Moj Algorytm')
    plt.plot(graphList, numerical_lib_result, label="Biblioteka Numeryczna")
    plt.yscale("log")
    plt.xscale("log")
    leg = plt.legend(loc="upper center")
    plt.grid()
    plt.show()

mojmorisson(50)
numerical(50)
showResults(50)
compute()
graph()












