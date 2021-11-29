import math
from functools import reduce
from random import randint


def min_max():
    lista = [randint(1, 100) for _ in range(10)]
    print(lista)
    print('minimum ', min(lista))
    print('maximum ', max(lista))


def suma_100_losowych_cyfr():
    lista = [randint(1, 100) for _ in range(100)]
    print('suma listy = ', sum(lista))
    return lista


def srednia_arytmetyczna(lista):
    print('średnia arytmetyczna = ', sum(lista) / len(lista))


def lista_dwuwymiarowa():
    n = 10

    lista = [[0 if x != y else x for x in range(n)] for y in range(n)]

    for row in lista:
        print(row)

    print('suma przekątnej = ', sum([lista[i][i] for i in range(n)]))


def lista_dwuwymiarowa2():
    n = 10

    lista = [[0 if x != (n - y - 1) else y for x in range(n)] for y in range(n)]

    for row in lista:
        print(row)

    print('suma przekątnej = ', sum([lista[i][n - i - 1] for i in range(n)]))


def dodawanie_2_macierzy():
    n = 10
    macierz1 = [[1 for _ in range(n)] for _ in range(n)]
    macierz2 = [[2 for _ in range(n)] for _ in range(n)]

    add_array = [[macierz1[x][y] + macierz2[x][y] for y in range(n)] for x in range(n)]
    for row in add_array:
        print(row)


def odejmowanie_2_macierzy():
    n = 10
    macierz1 = [[1 for _ in range(n)] for _ in range(n)]
    macierz2 = [[2 for _ in range(n)] for _ in range(n)]

    add_array = [[macierz2[x][y] - macierz1[x][y] for y in range(n)] for x in range(n)]
    for row in add_array:
        print(row)


def mnozenie_2_macierzy():
    n = 10
    macierz1 = [[1 for _ in range(n)] for _ in range(n)]
    macierz2 = [[2 for _ in range(n)] for _ in range(n)]

    add_array = [[macierz2[x][y] * macierz1[x][y] for y in range(n)] for x in range(n)]
    for row in add_array:
        print(row)


def czworka_pitagorejska():
    n = 20
    lista_czworek = [(a, b, c, d) for a in range(1, n) for b in range(a, n) for c in range(b, n) for d in range(c, n) if
                     (a * a + b * b + c * c == d * d)]

    for row in lista_czworek:
        print(row)


def eval_nauka():
    # wyrazenie = input('wyrazenie> ')
    # print(eval(wyrazenie))

    lista = [i + 1 for i in range(6)]
    with open('1.txt', 'w') as f:
        f.write(str(lista))

    with open('1.txt', 'r') as f:
        lista = eval(f.read())

    print(sum(lista))


f = lambda x: x % 2 != 0 and x % 3 != 0


def filter_liczby_pierwsze():
    pierwsze = list(filter(f, range(10, 25)))
    print(pierwsze)


szczescian = lambda x: x * x * x


def map_szescian():
    liczby = list(map(szczescian, range(1, 15)))
    liczby_filter = list(filter(szczescian, range(1, 15)))
    print(liczby)
    print(liczby_filter)


def oblicz_sume_wyrazenia():  # 1 + 2 - 3 + 4 - 5 + ... +- n = ....
    n = 20
    liczby = sum(map(lambda x: (1 - 2 * (x % 2)) * x, range(1, n + 1))) + 2
    print(liczby)


def oblicz_wyrazenie1():  # (2n-1)
    n = 100
    liczby = sum(map(lambda x: (2 * x - 1), range(1, n + 1)))
    print(liczby)


dodaj = lambda x, y: x + y


def dodawanie_reduce():
    print(reduce(dodaj, range(1, 101)))


def przyblizona_e(n):
    return reduce(lambda x, y: (x[0] + x[1], x[1] / y), range(1, n), (0, 1.0))


def przyblizona_wartosc_e():
    print("stała e = ", math.e)
    print('przyblizona wartosc e = ', przyblizona_e(20))

def zip_laczenie_list_parzystych_i_nieparzystych():
    lista_parzysta = [2,4,6,8,10]
    lista_nieparzysta = [1,3,5,7,9]

    print(list(zip(lista_nieparzysta,lista_parzysta)))


if __name__ == '__main__':
    # zip_laczenie_list_parzystych_i_nieparzystych()
    l = [1,2,3]
    lista = [x * [3, 5,6][x % 3] for x in l]
    print(lista)
