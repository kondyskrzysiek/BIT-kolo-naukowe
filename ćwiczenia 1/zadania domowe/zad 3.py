from os import listdir,mkdir,walk
from shutil import move

def sprawdzaniePliku(lista_plikow):
    for plik in lista_plikow:
        for index , letters in enumerate(plik):
            if letters == '.':
                if plik[index:] != '.py':
                    mkdir(plik[index+1:])
                    for p in lista_plikow:
                        if p.count(plik[index:]):
                            move(p,plik[index+1:])
                            print(f'przeniesie pliku {p} do {plik[index+1:]} ')
                return


if __name__ == '__main__':
    for subdir, dirs, files in walk('./'):
        del dirs[:]

    while len(files)>1:
        sprawdzaniePliku(files)

        for subdir, dirs, files in walk('./'):
            del dirs[:]