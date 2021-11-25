import itertools
import operator
import functools


def mnozenie_2_list():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [6, 7, 8, 9, 0]
    print('wynik ', list(map(operator.mul, lista1, lista2)))


def dodawanie_2_list():
    lista1 = [1, 2, 3, 4, 5]
    lista2 = [6, 7, 8, 9, 0]
    print('wynik ', list(map(operator.add, lista1, lista2)))


def count_dzialanie():  # itertools.count(start,krok)       range(start,koniec,krok)
    for i in itertools.count(2, 2):
        if i == 30:
            break
        else:
            print(i)


def cycle_dzialanie():
    licznik = 0
    for i in itertools.cycle('MSK'):
        if licznik >= 12:
            break
        else:
            print(i, end=' ')
            licznik += 1


def repeat_dzialanie():
    print(list(itertools.repeat(20, 6)))


def product_dzialanie_iloczyn_kartezjanski():
    lista1 = [0, 1, 2, 3]
    lista = ['Ząb', 'za', 'ząb']
    lancuch1 = 'ABC'
    lancuch2 = 'MSK'
    lista2 = [3, 4]

    # print(list(itertools.product(lista1,repeat = 3)))
    # print(list(itertools.product(lista,lancuch1)))
    # print(list(itertools.product(lancuch2,lista2)))


def permutations_dzialanie():
    lista = [1, 'ząb']
    lancuch = 'MSK'

    print(list(itertools.permutations(lista)))
    print(list(itertools.permutations(lancuch)))
    print(list(itertools.permutations(range(3), 2)))


def combinations_dzialanie():
    lista = [1, 'A']
    lancuch = 'MSK'

    print(list(itertools.combinations(lista, 2)))
    print(list(itertools.combinations(lancuch, 2)))
    print(list(itertools.combinations(range(4), 2)))


def combinations_with_replecment_dzialanie():
    lista = [1, 'A', 'k']
    lancuch = 'MSK'

    print(list(itertools.combinations_with_replacement(lista, 3)))
    print(list(itertools.combinations_with_replacement(lancuch, 2)))
    print(list(itertools.combinations_with_replacement(range(3), 2)))


#
# ITERATORY SKOŃCZONE
#

def accumulate_i_reduce_dzialanie():
    lista = [1, 2, 3, 4, 5]
    #accumulate prezentuje wyniki też pośrednie
    print('dzialanie accumulate to ', list(itertools.accumulate(lista, lambda x, y: x + y)))

    #reduce prezentuje wynik końcowy tylko
    print('dzialanie reduce to ', functools.reduce(lambda x, y: x + y, lista))

def chain_dzialanie():
    #funkcja łączy obiekty iterowalne
    lista = [1, 2, 3, 4, 5]
    lista1 = [2,3,4,5,6]
    lista2 = [3,4,5,6,7]
    print(list(itertools.chain(lista,lista1, lista2)))

def compress_dzialanie():
    lancuch = 'ZĄBZAZĄB'
    lista = [1,0,0,0,1,1,0,0]

    print(list(itertools.compress(lancuch,lista)))

def dropwhile_dzialanie():
    lista = [2,4,5,7,9]

    print(list(itertools.dropwhile(lambda x:x%2 == 0 ,lista)))

def filterfalse_dzialanie():
    lista = [2,4,5,7,9]

    print(list(itertools.filterfalse(lambda x : x % 2 == 0 ,lista)))

def islice_dzialanie():
    lista = [2,5,6,2,9,11,20,13]
    print(list(itertools.islice(lista,1,6,2)))

def takewhile_dzialanie():
    #dopóki lista nie zwróci False to funkcja się będzie wykonywać
    lista = [2,4,6,7,8,10]
    print(list(itertools.takewhile(lambda x: x % 2 == 0 , lista)))

if __name__ == "__main__":
    takewhile_dzialanie()
