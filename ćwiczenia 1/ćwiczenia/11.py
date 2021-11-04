if __name__ == '__main__':
    while True:
        lista =[]
        string = input('<<napisz działanie ze spacjami pomiędzy cyframi a operatorem >> \n <<jeżeli chceesz zakończyć napisz exit>>\n')
        if string == 'exit':
            break
        for i in string.split(" "):
            lista.append(i)

        if lista[1] == '+':
            print("wynik = ",float(lista[0]) + float(lista[2]))
        elif lista[1] == '-':
            print("wynik = ",float(lista[0]) - float(lista[2]))
        elif lista[1] == '*':
            print("wynik = ",float(lista[0]) * float(lista[2]))
        elif lista[1] == '/':
            print("wynik = ",float(lista[0]) / float(lista[2]))
        elif lista[1] == '^':
            print("wynik = ",float(lista[0]) ** float(lista[2]))