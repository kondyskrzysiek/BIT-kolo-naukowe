def krotki_wypisywanie_pojedynczo_petla_for():
    imiona = ('max', 'filip', 'karina', 'maria', 'karolina',)

    for imie in imiona:
        print(imie)


def krotki_wypisywanie_pojedynczo_petla_for_indexowanie():
    imiona = ('max', 'filip', 'karina', 'maria', 'karolina',)

    for index in range(len(imiona)):
        print(imiona[index])


def zamiana_listy_na_krotke():
    lista = [1, 2, 3, 4]
    krotka = tuple(lista)
    print(krotka)


def zamiana_krotki_na_liste():
    krotka = (1, 2, 3, 4,)
    lista = list(krotka)
    print(lista)


def kontakenacja_krotek():
    krotka1 = (1, 2, 3, 4,)
    krotka2 = (10, 20, 30, 40,)

    print("kontakenacja krotek ", krotka1 + krotka2)


def sortowanie_imion():
    krotka_imoiona = ('Jakub', 'Bartosz', 'Max', 'Filip',)
    sort_imiona_lista = list(krotka_imoiona)
    sort_imiona_lista.sort()
    krotka_imoiona = tuple(sort_imiona_lista)
    print("posortowana krotka : ", krotka_imoiona)


def dzialanie_srednia_arytmetyczna_dwuelementowej_krotki(a, b):
    return (a + b) / 2.0


def srednia_arytmetyczna_dwuelementowej_krotki():
    (a, b,) = (11.5, 12.6,)
    print(f'srednia arytmetyczna krotki a = {a} , b = {b} jest równa = {dzialanie_srednia_arytmetyczna_dwuelementowej_krotki(a, b)}')

def suma_krotki():
    krotka = (1,2,3,4,5,)
    print('suma krotki = ',sum(krotka))

def zagniezdzona_krotka_i_suma_przekatnej():
    n = 10
    lista_nxn = [[0 if not x == y else 1 for x in range(n)] for y in range(n)]

    print('lista')
    for row in lista_nxn:
        print(row)

    krotka_nxn = tuple(tuple(row) for row in lista_nxn)

    print('krotka')
    for row in krotka_nxn:
        print(row)

    print('suma przekątnej = ',sum(list(krotka_nxn[i][i] for i in range(n))))

def zapis_i_odczyt_krotki_z_pliku_txt():
    krotka = (1, 2, 3, 4,)
    with open('krotka.txt', 'w') as f:
        f.write(str(krotka))

    with open('krotka.txt', 'r') as f:
        krotka_odczyta = tuple(eval(f.read()))

    print(krotka)
    print('suma krotki początkowej = ', sum(krotka))
    print(krotka_odczyta)
    print('suma krotki odczytanej = ',sum(krotka_odczyta))




if __name__ == "__main__":
    pass