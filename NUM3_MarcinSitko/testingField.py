import numpy as np
from timeit import default_timer as timer
import scipy
import scipy.sparse
from  functools import reduce
from matplotlib import pyplot as plt

# Tworzenie macierzy 100x100 na potrzeby, policzenia wyniku zadania biblioteka nuemryczna
def definingMatrix(n):
    #Diagonal
    diag = np.empty(n)
    diag.fill(1.2)

    # 1sub diagonal
    sub1diag = np.empty(n)
    sub1diag.fill(0.2)

    #1above diagonal
    abv1diag = np.empty(n)
    for i in range(1,len(abv1diag)):
        abv1diag[i]  =(0.1)/(i)

    #2above diagonal
    abv2diag = np.empty(n)
    for j in range(0,len(abv2diag)):
       if j > 1 :
        abv2diag[j] = (0.4)/((j-1)**2)
       else:
           abv2diag[j] = 0

    diag_rows = []
    diag_rows.append(sub1diag)
    diag_rows.append(diag)
    diag_rows.append(abv1diag)
    diag_rows.append(abv2diag)

    size = n
    vals = [sub1diag,diag, abv1diag, abv2diag]
    offset=-1
    res = reduce(lambda a, b: a+np.eye(n,k=b[0]+offset)*b[1], enumerate(vals), np.zeros((n, n)))

    return res
#Tworzenie macierzy 4x100 na potrzeby policzenia rozkladu LU
def customMatrix(n):
    # Diagonal
    diag = np.empty(n)
    diag.fill(1.2)

    # 1sub diagonal
    sub1diag = np.empty(n)
    sub1diag.fill(0.2)

    # 1above diagonal
    abv1diag = np.empty(n)
    for i in range(1, len(abv1diag)):
        abv1diag[i] = (0.1) / (i)

    # 2above diagonal
    abv2diag = np.empty(n)
    for j in range(0, len(abv2diag)):
        if j > 1:
            abv2diag[j] = (0.4) / ((j - 1) ** 2)
        else:
            abv2diag[j] = 0


    return diag,sub1diag[1:],abv1diag[1:],abv2diag[2:]
def definingVector(n):
    x = np.arange(1,n+1).reshape(n,1)
    return x
def doolittle(diag,sub1diag,abv1diag,abv2diag):
    n = diag.shape[0]
    U = np.zeros((n,n))
    L = np.eye(n)
    for k in range(n-2):
        U[k,k] = diag[k] - np.dot(L[k,(k-1)],U[k-1,k])
        L[(k + 1), k] = sub1diag[k] / U[k, k]
        U[k, (k + 1)] = abv1diag[k] - np.dot(L[k, (k - 1)], U[(k - 1), (k + 1)])
        U[k, (k + 2)] = abv2diag[k]
        if k>n-4:
            U[k+1, k+1] = diag[k] - np.dot(L[k+1,k],U[k,k+1])
            L[k+2, k+1] =sub1diag[k] / U[k+1,k+1]
            U[k+1, k+2] = abv1diag[k+1] - np.dot(L[k+1,k],U[k,k+2])
            U[k+2, k+2] = diag[k] - np.dot(L[k+2, k+1], U[k+1, k+2])
    return L,U

def forwSub(L,b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
    return y
def backSub(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n - 2, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i:], x[i:])) / U[i, i]
    return x

#Funckja Sprawdzajaca poprawnosc wynikow mojego algorytmu w porowaniu do wynikow bilbioteki numerycznej
def checkResults():
    print("\nPorownanie wynikow rozwiazania rownania macierzowego")
    print("Rozwiazanego przez bilioteki numeryczna 'numpy' oraz rozwiazanego przez moj wyspecjalizowany algorytm "
          "\nrozkladu LU oraz backsubstitution oraz forwardsubstitution")

    # Tworzenie macierzy
    matrix1 = definingMatrix(100)
    diag,sub1,abv1,abv2 = customMatrix(100)

    # Tworzenie wektora wyrazow wolnych
    vector1 = definingVector(100)

    # Obliczenie rownania macierzowego Ax=b za pomoca biblioteki numerycznej
    l_numeric,u_numeric = scipy.linalg.decomp_lu.lu(matrix1,permute_l=True)
    x_numeric  = forwSub(l_numeric,vector1)
    y1 = backSub(u_numeric,x_numeric)
    L, U = doolittle(diag,sub1,abv1,abv2)
    x = forwSub(L, vector1)
    y2 = backSub(U, x)

    # Wyniki Z bilioteki numerycznej
    print()
    print("Wynik Rownania macierzowego obliczonego poprzez biblioteke numeryczną ")
    for i in range(len(y1)):
        if i % 20 == 0:
            print()
        print(y1[i], end=" ")

    print("\n\n")
    # Wyniki Z mojego algorytmu Rozkladu LU , back substitution , forward substitution
    print("Wynik Rownania macierzowego obliczonego Algorytmem wyspecjalizowanym ")
    for i in range(len(y2)):
        if i % 20 == 0:
            print()
        print(y2[i], end=" ")

    # Roznica wyniku bilbioteki numeryczej oraz mojego wyspecjalizowanego alogyrtmu rozkladu LU
    print("\n\nSprawdzenie Poprawnosci Obliczen, vektor powinien byc bardzo bliski zeru")
    checking_result = y1 - y2
    for k in range(len(checking_result)):
        if k % 20 == 0:
            print()
        print(checking_result[k], end=" ")

#Funkcja Sprawdzajaca czas wykonania rozkladu LU mojego algorytmu oraz algorytmu biblioteki numerycznej
def main():
    #Tworzenie macierzy
    matrix1 = definingMatrix(100)
    #Tworzenie wektora wyrazow wolnych
    vector1 = definingVector(100)

    #Obliczenie rownania macierzowego Ax=b za pomoca biblioteki numerycznej
    t0 = timer()
    l_numeric, u_numeric = scipy.linalg.decomp_lu.lu(matrix1,permute_l=True)
    x_numeric = forwSub(l_numeric, vector1)
    y1 = backSub(u_numeric, x_numeric)
    t1 = timer()

    print("CZAS WYKONANIA ROWNANIA MACIERZOWEGO")
    #Wypisanie czasu potrzebnego na wykonanie sie algorytmu
    numerical_lib_time = np.float64(t1-t0)
    print("Bilbioteka numeryczna: ",numerical_lib_time)

    diag, sub1, abv1, abv2 = customMatrix(100)
    #Obliczenie rownania macierzowego Ax=b za pomoca faktoryzacji  - rozkladu LU
    t2 = timer()
    L,U = doolittle(diag,sub1,abv1,abv2)
    x = forwSub(L,vector1)
    y2= backSub(U,x)
    t3 = timer()

    #Wypisanie czasu potrzebnego na wykonanie sie algorytmu
    mytime = np.float64(t3-t2)
    print("Moj Wyspecjalizowny algorytm: ",mytime)

# Tablice przechowujace dane, o czasach wykonania algorytmow tak aby nie trzebaby bylo za kazdym razem go wykonywac
# Wystarczy jednorazowe uruchomienie obliczen i tablice zostana wypelnione danymi
myresult = []
numerical_lib_result = []
graphList = []

#Funkcja Odpowiadajaca za policzenie czasu wykonania alogrytmow dla 100 <= n < 5000 z krokiem 600
def compute():
    print("\nRozwiazanie Rownanian macierzowych dla 100<n<5.000 z krokiem 600")

    print("\n Rozwiazywanie tych rownan moze zajac kilkanascie sekund prosze o cierpliwosc")
    for n in range(100, 5000, 600):
        matrix1 = definingMatrix(n)
        graphList.append(n)

        # Tworzenie wektora wyrazow wolnych
        vector1 = definingVector(n)

        # Obliczenie rownania macierzowego Ax=b za pomoca biblioteki numerycznej
        t0 = timer()
        l_numeric, u_numeric = scipy.linalg.decomp_lu.lu(matrix1,permute_l=True)
        x_numeric = forwSub(l_numeric, vector1)
        y1 = backSub(u_numeric, x_numeric)
        t1 = timer()

        print("\n n = ",n)
        # Wypisanie czasu potrzebnego na wykonanie sie algorytmu
        numerical_lib_time = np.float64(t1 - t0)
        numerical_lib_result.append(numerical_lib_time)
        print("Czas Bilioteki Numerycznej: ", numerical_lib_time)

        diag, sub1, abv1, abv2 = customMatrix(n)
        # Obliczenie rownania macierzowego Ax=b za pomoca faktoryzacji  - rozkladu LU
        t2 = timer()

        L, U = doolittle(diag,sub1,abv1,abv2)
        x = forwSub(L, vector1)
        y2 = backSub(U, x)
        t3 = timer()

        # Wypisanie czasu potrzebnego na wykonanie sie algorytmu
        mytime = np.float64(t3 - t2)
        myresult.append(mytime)
        print("Czas Mojego Algorytmu rozkladu : ",mytime)


#Funkcja ktora umolliwia uzytkownikowi ponowne sprawdzenie czasow wykonania obliczen
def showResultsMore():
    for i in range(len(myresult)):
        print("MyTime: ", myresult[i])
    for j in range(len(numerical_lib_result)):
        print("Numercial module time: ", numerical_lib_result[j])

def matrixDet():
    diag, sub1, abv1, abv2 = customMatrix(100)
    L, U = doolittle(diag, sub1, abv1, abv2)
    matrix = definingMatrix(100)
    det = np.linalg.det(U)
    print("Wyznacznik Macierzy z zadania U  to: ",det)

#Funkcja Pokazujaca Graf, z czasem wykonania obliczen
def graph():
    plt.title("Zaleznosc czasu wykonania sie algorytmu od wielkosci macierzy ")
    plt.xlabel("Wielkosc Macierzy")
    plt.ylabel("Czas Wykonania algorytmu (s)")
    plt.plot(graphList, myresult, label='Moj Algorytm')
    plt.plot(graphList, numerical_lib_result, label="Biblioteka Numeryczna")
    leg = plt.legend(loc="upper center")
    plt.grid()
    plt.show()

# main()
# compute()
# checkResults()
# showResultsMore()
# graph()