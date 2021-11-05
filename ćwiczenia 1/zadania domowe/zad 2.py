from sys import exit

def drawSzachownica(ls):

    print('1,2,3\n4,5,6\n7,8,9')
    print(f'-------\n|{ls[0]}|{ls[1]}|{ls[2]}|\n-------\n|{ls[3]}|{ls[4]}|{ls[5]}|\n-------\n|{ls[6]}|{ls[7]}|{ls[8]}|\n-------\n')

def sprawdzanieWygranej(ls,gracz):
    if ls[0]==ls[1]==ls[2] != ' ' or ls[3]==ls[4]==ls[5] != ' ' or ls[6]==ls[7]==ls[8] != ' ' or ls[0]==ls[3]==ls[6] != ' ' or ls[1]==ls[4]==ls[7] != ' 'or ls[2]==ls[5]==ls[8] != ' 'or ls[0]==ls[4]==ls[8] != ' ' or ls[2]==ls[4]==ls[6] != ' ':
        drawSzachownica(ls)
        print(f'!!!wygrana gracza {gracz}!!!!!')
        exit(0)

if __name__ == '__main__':
    gracz = 'x'
    posuniecie = 0
    szachownica = []

    for i in range(9):
        szachownica.append(' ')

    while szachownica.count(' '):

        drawSzachownica(szachownica)

        wyborgraczaX = int(input(f'podaj pole gracz "{gracz}" : '))

        if wyborgraczaX>=1 and wyborgraczaX <=9:
            if szachownica[wyborgraczaX-1] != ' ':
                print('\n\n\n!!wybierz inne pole ponieważ te jest już wybrane!!\n\n\n')
            else:
                szachownica[wyborgraczaX-1] = gracz
                if posuniecie == 4:
                    sprawdzanieWygranej(szachownica,gracz)
                else:
                    posuniecie += 1

                if gracz == 'x':
                    gracz = 'o'
                else:
                    gracz = 'x'

                print(szachownica,gracz,posuniecie)

    drawSzachownica(szachownica)
    print('nie ma już wolnych pól')