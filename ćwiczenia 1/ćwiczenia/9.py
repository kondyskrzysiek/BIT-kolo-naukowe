from random import randint

def filtrowanie(lista):
    filtrlista = []
    for elem in lista:
        if elem >= 10:
            filtrlista.append(elem)
    print(filtrlista)

if __name__ == '__main__':
    lista = []
    for i in range(0,10):
        lista.append(randint(-5,20))
    print(lista)
    filtrowanie(lista)
