from os import mkdir,walk
from shutil import move

def przenoszenie_plikow(lista_plikow):
    while len(lista_plikow) > 0:
        listaremove = []
        plik = lista_plikow[0]
        for index , letters in enumerate(plik):
            if letters == '.':
                mkdir(plik[index+1:],exist_ok=True)
                for plik_przeniesienie in lista_plikow:
                    if plik_przeniesienie.count(plik[index:]):
                        move(plik_przeniesienie,plik[index+1:])
                        listaremove.append(plik_przeniesienie)
                for file in listaremove:
                    lista_plikow.remove(file)

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
    files = zczytywanie_folderow_plikow()
    przenoszenie_plikow(files)