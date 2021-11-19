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
    krotka_imoiona = ('Jakub','Bartosz','Max','Filip',)
    sort_imiona_lista = list(krotka_imoiona)
    sort_imiona_lista.sort()
    krotka_imoiona = tuple(sort_imiona_lista)
    print("posortowana krotka : ",krotka_imoiona)

if __name__ == "__main__":
    sortowanie_imion()