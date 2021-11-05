def sprawdzanieStringa(string,substring):
    zliczanie_substring = 0
    lista_substring = []
    l = 0
    a = 0
    while True:
        l = string.find(substring)
        if l>=0:
            a += l+1
            zliczanie_substring += 1
            lista_substring.append(a)
            if l == 0:
                string = string[1:]
            else:
                string = string[l + 1:]
        else:
            break
    print('Wynik: ', zliczanie_substring)
    print('occurrences : ', lista_substring)

if __name__ == '__main__':
    string = input('podaj string: ')
    substring = input('podaj substring: ')

    sprawdzanieStringa(string, substring)