import numpy as np
from matplotlib import pyplot as plt



def a_floatPrecision():
    h = []
    starting_index = 1.9
    h.append(starting_index)

    # Counting value of equation for every h
    for i in range(440):
        h.append(np.float32(h[i]*0.95))

    x = np.float32(0.2)
    fx = np.float32(np.sin(x))
    fx_derivative = np.float32(np.cos(x))
    result = []

    for j in range(len(h)):
        equation = np.float32(abs(((np.sin(x+h[j]) - fx) / (h[j])) - fx_derivative))
        result.append(equation)

    # Plotting
    plt.title("Podpunkt A) Wykres dla precyzji FLOAT")
    plt.plot(h, result, color="green")
    plt.xlabel("Wartosci h")
    plt.ylabel("Wartosc Błedu")
    plt.grid()
    plt.yscale("log")
    plt.xscale("log")
    plt.show()



def a_doublePrecision():
    h = []
    starting_index = 1.9
    h.append(starting_index)

    # Counting value of equation for every h
    for i in range(1040):
        h.append(np.float64(h[i] * 0.95))

    x = np.float64(0.2)
    fx = np.float64(np.sin(x))
    fx_derivative = np.float64(np.cos(x))
    result = []

    for j in range(len(h)):
        equation = np.float64(abs(((np.sin(x + h[j]) - fx) / (h[j])) - fx_derivative))
        result.append(equation)


    # Plotting
    plt.title("Podpunkt A) Wykres dla precyzji DOUBLE")
    plt.plot(h, result,color="blue")
    plt.xlabel("Wartosci h")
    plt.ylabel("Wartosc Błedu")
    plt.grid()
    plt.yscale("log")
    plt.xscale("log")
    plt.show()



def b_floatPrecision():
    h = []
    starting_index = 1.9
    h.append(starting_index)

    # Counting value of equation for every h
    for i in range(440):
        h.append(np.float32(h[i]*0.95))

    x = np.float32(0.2)
    fx = np.float32(np.sin(x))
    fx_derivative = np.float32(np.cos(x))
    result = []

    for j in range(len(h)):
        equation = np.float32(abs(((np.sin(x+h[j]) - np.sin(x-h[j])) / (2*h[j])) - fx_derivative))
        result.append(equation)

    # Plotting
    plt.title("Podpunkt B) Wykres dla precyzji FLOAT")
    plt.plot(h, result, color="green")
    plt.xlabel("Wartosci h")
    plt.ylabel("Wartosc Błedu")
    plt.grid()
    plt.yscale("log")
    plt.xscale("log")
    plt.show()


def b_doublePrecision():
    h = []
    starting_index = 1.9
    h.append(starting_index)

    # Counting value of equation for every h
    for i in range(1040):
        h.append(np.float64(h[i]*0.95))

    x = np.float64(0.2)
    fx = np.float64(np.sin(x))
    fx_derivative = np.float64(np.cos(x))
    result = []

    for j in range(len(h)):
        equation = np.float64(abs(((np.sin(x+h[j]) - np.sin(x-h[j])) / (2*h[j])) - fx_derivative))
        result.append(equation)

    # Plotting

    plt.title("Podpunkt B) Wykres dla precyzji DOUBLE")
    plt.plot(h, result, color="blue")
    plt.xlabel("Wartosci h")
    plt.ylabel("Wartosc Błedu")
    plt.grid()
    plt.yscale("log")
    plt.xscale("log")
    plt.show()


def experimental():
    h = []
    starting_index = 1.9
    h.append(starting_index)

    # Counting value of equation for every h
    for i in range(440):
        h.append(np.float32(h[i]*0.95))

    x = np.float32(0.2)
    fx = np.float32(np.cos(x))
    fx_derivative = -np.float32(np.sin(x))
    result = []

    for j in range(len(h)):
        equation = np.float32(abs(((np.cos(x+h[j]) - fx) / (h[j])) - fx_derivative))
        result.append(equation)

    # Plotting
    plt.title("exp(x) x = 0.2 typ:FLOAT")
    plt.plot(h, result, color="green")
    plt.xlabel("Wartosci h")
    plt.ylabel("Wartosc Błedu")
    plt.grid()
    plt.yscale("log")
    plt.xscale("log")
    plt.show()


def experimental1():
    h = []
    starting_index = 1.9
    h.append(starting_index)

    # Counting value of equation for every h
    for i in range(440):
        h.append(np.float32(h[i]*0.95))

    x = np.float32(5)
    fx = np.float32(np.exp(x))
    fx_derivative = np.float32(np.exp(x))
    result = []

    for j in range(len(h)):
        equation = np.float32(abs(((np.exp(x+h[j]) - fx) / (h[j])) - fx_derivative))
        result.append(equation)

    # Plotting
    plt.title(" exp(x) x = 5 typ:FLOAT")
    plt.plot(h, result, color="green")
    plt.xlabel("Wartosci h")
    plt.ylabel("Wartosc Błedu")
    plt.grid()
    plt.yscale("log")
    plt.xscale("log")
    plt.show()

def experimental2():
    h = []
    starting_index = 1.9
    h.append(starting_index)

    # Counting value of equation for every h
    for i in range(440):
        h.append(np.float32(h[i]*0.95))

    x = np.float32(50)
    fx = np.float32(np.exp(x))
    fx_derivative = np.float32(np.exp(x))
    result = []

    for j in range(len(h)):
        equation = np.float32(abs(((np.exp(x+h[j]) - fx) / (h[j])) - fx_derivative))
        result.append(equation)

    # Plotting
    plt.title(" exp(x) x = 50 typ:FLOAT")
    plt.plot(h, result, color="green")
    plt.xlabel("Wartosci h")
    plt.ylabel("Wartosc Błedu")
    plt.grid()
    plt.yscale("log")
    plt.xscale("log")
    plt.show()



# All the functions
#a_floatPrecision()
#a_doublePrecision()
#b_floatPrecision()
#b_doublePrecision()
# experimental()
# experimental1()
# experimental2()
