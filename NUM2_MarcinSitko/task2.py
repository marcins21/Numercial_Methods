import numpy as np
import numpy.linalg
from matplotlib import pyplot as plt

#Defining Matrix's
A1 = np.array([[2.34332898,-0.11253278,-0.01485349,0.33316649,0.71319625],
     [-0.11253278,1.67773628,-0.32678856,-0.31118836,-0.43342631],
     [-0.01485349, -0.32678856, 2.66011353, 0.85462464, 0.16698798],
     [0.33316649, -0.31118836, 0.85462464, 1.54788582, 0.32269197],
     [0.71319625, -0.43342631, 0.16698798, 0.32269197, 3.27093538]])
A1 = A1.astype("float64")

A2 = np.array([[2.34065520, -0.05353743, 0.00237792, 0.32944082, 0.72776588],
    [-0.05353743, 0.37604149, -0.70698859, -0.22898376, -0.75489595],
    [0.00237792, -0.70698859, 2.54906441, 0.87863502, 0.07309288],
    [0.32944082, -0.22898376, 0.87863502, 1.54269444, 0.34299341],
    [0.72776588, -0.75489595, 0.07309288, 0.34299341, 3.19154447]])
A2 = A2.astype("float64")

b1 = np.array([3.55652063354463,-1.86337418741501,5.84125684808554,-1.74587299057388,0.84299677124244])
b1 = b1.astype("float64")

b2 = np.array([1e-5,0,0,0,0])
b2 = b2.astype("float64")

b_prim = np.add(b1,b2)
b_prim = b_prim.astype("float64")




#Print Function
def print_matrix(matrix:int):
    if matrix == 1:
        print("\nA1")
        for i in range(len(A1)):
            for j in range(len(A1)):
                print(A1[i][j],end=", ")
            print()
    elif matrix == 2:
        print("\n\nA2")
        for i in range(len(A2)):
            for j in range(len(A2)):
                print(A2[i][j],end=", ")
            print()
    elif matrix == 3:
        print("\nb")
        for i in range(len(b1)):
            print(b1[i],end=", ")
    elif matrix == 4:
        print("\n\nb'")
        for i in range(len(b_prim)):
            print(b_prim[i],end=", ")
        print()


def show_results():
    print("Wynik Rownania A1x=b")
    x = np.linalg.solve(A1,b1)
    print("x1 ",x)

    print("Wynik Rownania A1x=b'")
    x2 = np.linalg.solve(A1,b_prim)
    print("x1' ",x2)

    print("Wynik Rownania A2x=b")
    x3 = np.linalg.solve(A2,b1)
    print("x2 ",x3)

    print("Wynik Rownania A2x=b'")
    x4 = np.linalg.solve(A2,b_prim)
    print("x2' ",x4)

    print("\n\n")

    print("||x1 - x1'|| = ",end=" ")
    dist = np.linalg.norm(x-x2)
    print(dist)

    print("||x2 - x2'|| = ",end=" ")
    dist2 = np.linalg.norm(x3-x4)
    print(dist2)

    print("Roznica Norm || x1  -  x1' || - || x2  -  x2' || = ",end=" ")
    print(dist - dist2)

    print("wspolczynnik kappa uwarunkowania macierzy A1 = ",end=" ")
    cond1 = np.linalg.cond(A1)
    print(cond1)

    print("Wspolczynnik kappa uwarunkowania macierzy A2 = ",end=" ")
    cond2 = np.linalg.cond(A2)
    print(cond2)

    # Kappa2 = 320 milionow 17 tysiecy  246
    print()

def additional():
    egv1 = np.linalg.eigvals(A1)
    egv2 = np.linalg.eigvals(A2)

    cond1 = max(egv1)/min(egv1)
    cond2 = max(egv2)/min(egv2)
    print("Wspolczynnik Uwarunkowania macierzy A1 policzony ręcznie: ",end=" ")
    print(cond1)
    print("Wspolczynnik Uwarunkowania macierzy A2 policzony ręcznie: ", end=" ")
    print(cond2)

    print()

    print("wspolczynnik kappa uwarunkowania macierzy A1 używajac funkcji cond()  ", end=" ")
    cond1 = np.linalg.cond(A1)
    print(cond1)

    print("Wspolczynnik kappa uwarunkowania macierzy A2 używajac funkcji cond()  ", end=" ")
    cond2 = np.linalg.cond(A2)
    print(cond2)
    print("")

#Functions
# print("Printing matrix's")
# for i in range(1,5):
#     print_matrix(i)
# show_results()
# additional()
#

