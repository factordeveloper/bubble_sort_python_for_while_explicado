## for while

def ordenar(numeros):
    n = len(numeros)
    for i in range(n):
        j = 0
        while j < n - i - 1:
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            j += 1
    print(numeros)

def main():
    entrada = [3, 5, 8, 9, 2, 7, 37]
    ordenar(entrada)

main()
