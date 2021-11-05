def dekodowanie(liczba_dziesietna):
    binarnaLista = []

    while True:
        binarnaLista.append(str(liczba_dziesietna % 2))
        liczba_dziesietna = int(liczba_dziesietna / 2)
        if liczba_dziesietna== 1:
            binarnaLista.append('1')
            break
        elif liczba_dziesietna == 0:
            break

    print('liczba binarna to >> ',''.join(binarnaLista[::-1]))

if __name__ == '__main__':
    liczba_dziesietna = int(input('podaj liczbe do konwersji z dzięsiętnej na binarną >> '))
    dekodowanie(liczba_dziesietna)