
import numpy as np
import functools

def main(n):
    hessenberg_matrix = [[3,6,6,9],
                         [1,4,0,9],
                         [0,0.2,6,12],
                         [0,0,0.1,6]]
    precision = (10)**(-15)

    #Wartosci walsne rozkladu QR (diag)
    result_QR = []

    def hessenbergQR():
        result_matrix = []
        # 200 Iteracji daje nam wystarczajaco dokladny wynik w algorytmie QR
        Q,R = np.linalg.qr(hessenberg_matrix)
        for i in range(n):
            new_matrix = np.dot(R,Q)
            Q_it,R_it = np.linalg.qr(new_matrix)
            R = R_it
            Q = Q_it
            result_matrix = new_matrix
        return result_matrix


    result_matrix = hessenbergQR()
    def checkingUnderDiag(result_matrix):
        #Sprawdzam liczby pod diagonala
        for i in range(len(result_matrix)):
            for j in range(i):
                if result_matrix[i][j] < precision:
                    result_matrix[i][j] = 0
        return result_matrix


    def w_wlasne(matrix):
        for i in range(len(matrix)):
            for j in range(i+1):
                if j == i:
                    result_QR.append(matrix[i][j])
                else:
                    pass


    #licze hessenberga
    result_matrix = hessenbergQR()
    #Licze przyblizenie pod diagonola z dokaldnosscia do precyzji
    result_matrix_checked = checkingUnderDiag(result_matrix)

    #Print Wynikow
    print("\nMacierz po przyblizonym rozkladzie QR\n")
    print(result_matrix_checked)

    #Licze Wartosci wlasne
    w_wlasne(result_matrix_checked)

    print("\nWartosci Wlasne Macierzy Hessenberga\n")
    print(result_QR) # Pokazuje te wartosci wlasne, zapisane zostaja do innej macierzy result_QR
    print()

#main(200)