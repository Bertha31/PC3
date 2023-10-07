import random

def generar_numeros():
    numeros_aleatorios = [random.randint(0, 100) for _ in range(20)]
    return numeros_aleatorios

def mostrar(lista):
    print("Lista de números:")
    for numero in lista:
        print(numero)

def ordenar(lista):
    lista_ordenada = sorted(lista)
    print("Lista ordenada:")
    for numero in lista_ordenada:
        print(numero)

if __name__ == "__main__":
    numeros_total = generar_numeros()
    mostrar(numeros_total)
    ordenar(numeros_total)

