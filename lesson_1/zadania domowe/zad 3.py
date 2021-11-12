from os import makedirs,walk
from shutil import move
from time import process_time

def przenoszenie_plikow(lista_plikow):
    while len(lista_plikow) > 0:
        listaremove = []
        plik = lista_plikow[0]
        print(plik)
        for index , letters in enumerate(plik[::-1]):
            print(letters)
            if letters == '.':
                print('wszedł')
                i = len(plik)-index
                makedirs(plik[i:],exist_ok=True)
                for plik_przeniesienie in lista_plikow:
                    if plik_przeniesienie.count(plik[i-1:]):
                        move(plik_przeniesienie,plik[i:])
                        listaremove.append(plik_przeniesienie)
                for file in listaremove:
                    lista_plikow.remove(file)
                break

def zczytywanie_folderow_plikow():
    for (root, dirs, files) in walk("./"):
        break

    should_restart = True
    while should_restart:
        should_restart = False
        for file in files:
            if file.count('.py'):
                files.remove(file)
                should_restart = True
                break
    return files

if __name__ == '__main__':
    a = process_time
    print()
    files = zczytywanie_folderow_plikow()
    przenoszenie_plikow(files)