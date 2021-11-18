def main():
    imiona = ['Jakub', 'Bartosz', 'Julia', 'Max', 'Agata']
    print(imiona)
    imie = input('imie jakie powinno zostać zamienione ? : ')
    try:
        imie_index = imiona.index(imie.title())
        nowe_imie = input('nowe imie : ')
        imiona.insert(imie_index, nowe_imie.title())
        print(imiona)
    except:
        print(imie, " nie znajduje się na liście")


if __name__ == '__main__':
    main()
