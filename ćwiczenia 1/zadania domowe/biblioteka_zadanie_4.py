from random import randint

def wypisanie_array(array):
    print('\n')
    for line in array:
        print(line)
    print('\n')

def tworzenie_array(n,m):
    array = []
    for i in range(n):
        wiersz = [randint(0,255) for _ in range(m)]
        array.append(wiersz)
    return array

def flip_horizontal(array):
    array_flip_horizontal = array[::-1]
    return array_flip_horizontal

def flip_vertical(array):
    array_flip_vertical = []
    for line in array:
        wiersz = line[::-1]
        array_flip_vertical.append(wiersz)

    return array_flip_vertical

def rotate(array,l_obrotow,n,m):
    if l_obrotow == 1:
        kierunek ='right'
    else:
        kierunek = 'left'
    while l_obrotow >=1:
        array_help = []
        for i in range(m):
            wiersz = [array[j][i] for j in range(n-1,-1,-1)]
            array_help.append(wiersz)
        array = array_help
        n , m = m , n
        l_obrotow -= 1

    return array_help,n,m

def reverse_array(array):
    array_help = []
    for line in array:
        wiersz = [255-digit for digit in line]
        array_help.append(wiersz)

    return array_help

def commandOpenDef(list,array,n,m):#flip_horizontal  ,   flip_vertical   ,  rotate_right   ,  rotate_left   ,   reverse_values
    for command in list:

        if command.lower() == 'done':
            print('\n\nwynik końcowy')
            wypisanie_array(array)
            break
        elif command.lower() == 'flip_horizontal':
            array = flip_horizontal(array)
        elif command.lower() == 'flip_vertical':
            array = flip_vertical(array)
        elif command.lower() == 'rotate_right':
            array,n,m = rotate(array,1,n,m)
        elif command.lower() == 'rotate_left':
            array,n,m = rotate(array,3,n,m)
        elif command.lower() == 'reverse_values':
            array = reverse_array(array)
        else:
            print('komenda nie zrozumiała: ',command)