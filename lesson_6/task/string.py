def iterowanie_string():
    imie = 'krzysztof'
    for i in imie:
        print(i)


def zliczanie_liter():
    ciag_words = 'MAtematyka jest królową wszystkich nauk.'
    dictionary = {}

    for znak in ciag_words:
        dictionary[znak.lower()] = dictionary.get(znak.lower(),0) + 1

    print('litera "a" występuje : ',dictionary['a'],' razy ')

def haslo_bezpieczenstwa():
    password = input('password: ')

    correct_length = False
    correct_upper_letter = False
    correct_lower_letter = False
    correct_digit = False

    if len(password) >= 7:
        correct_length = True

    for ch in password:
        if ch.islower():
            correct_lower_letter = True
        if ch.isupper():
            correct_upper_letter = True
        if ch.isdigit():
            correct_digit = True


    if correct_digit and correct_length and correct_lower_letter and correct_upper_letter:
        print('Password is correct')
    else:
        print('password is incorrect')

def piramids_0():
    n = 9
    for i in range(1,n+1):
        print('0'*i)
    for i in range(n-1,0,-1):
        print('0'*i)

def podzial_tekstu():
    tekst_imiona = 'Max dorota Filip Jadwiga'
    lista_imion = tekst_imiona.title().split()
    print(lista_imion)

if __name__ == "__main__":
    pass