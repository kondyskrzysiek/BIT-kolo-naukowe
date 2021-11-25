def add(a: int, b: int) -> int:
    if a == 0:
        return b
    else:
        return add(a - 1, b + 1)


def main_add():
    print(add(10, 15))


def szukanie_liczby(lista, szukana, pozycja):
    if lista[pozycja] == szukana:
        return f'znaleziono liczbe {szukana} na pozycji {pozycja + 1} rekurencyjnie'
    elif pozycja == len(lista) - 1:
        return f'nie znaleziono liczby {szukana}'
    return szukanie_liczby(lista, szukana, pozycja + 1)


def main_def_szukanie_liczby():
    lista = [1, 2, 5, 6, 8, 11, 15, 20, 30, 12, 12, 13, 4]
    szukana = 4

    try:
        print(f'znaleziono liczbe {szukana} na pozycji {lista.index(szukana) + 1}')
    except ValueError:
        print('nie znaleziono ', szukana)

    print(szukanie_liczby(lista, szukana, 0))  # rekurencyjnie


def wyszukiwanie_liczb(lista, szukana, poczatek,koniec):
    print(lista[poczatek:koniec],poczatek,koniec)
    if poczatek > koniec: return False
    pozycja = (poczatek + koniec) / 2

    if lista[int(pozycja)] == szukana:
        return f'znaleziono {szukana} na pozycji {int(pozycja)+ 1}'
    elif lista[int(pozycja)] < szukana:
        return wyszukiwanie_liczb(lista, szukana, int(pozycja),koniec)
    elif lista[int(pozycja)] > szukana:
        return wyszukiwanie_liczb(lista, szukana, poczatek,int(pozycja))


def main_wyszukiwanie_liczby():
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    cel = 7
    poczatek = 0
    koniec = len(lista)

    print(wyszukiwanie_liczb(lista, cel, poczatek,koniec))


if __name__ == "__main__":
    main_wyszukiwanie_liczby()
