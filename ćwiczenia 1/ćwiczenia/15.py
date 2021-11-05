from os import listdir

def sprawdzaniePy(pliki):
    iloscPy = 0
    for plik in pliki:
        if len(plik) > 3:
            if plik[-3:] == '.py' : iloscPy += 1
    print(iloscPy)

if __name__ == '__main__':
    print(listdir())
    sprawdzaniePy(listdir())