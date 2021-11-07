from biblioteka_zadanie_4 import *

if __name__ == '__main__':

    n = int(input('podaj użytkowniku liczbe wierszy macierzy : '))
    m = int(input('podaj użytkowniku liczbe kolumn macierzy : '))

    array = tworzenie_array(n,m)
    wypisanie_array(array)

    command = input('>>podaj liste komend po koleji odzielone pomiędzy spacją , linie komend zakończ komendą "done"<<\n'
                    '>>flip_horizontal  ,   flip_vertical   ,  rotate_right   ,  rotate_left   ,   reverse_values<<\n'
                    '>>')
    commandList = command.split()
    commandOpenDef(commandList,array,n,m)