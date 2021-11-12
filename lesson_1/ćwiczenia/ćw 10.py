if __name__ == '__main__':
    lista =[]
    string = input('<<napisz działanie ze spacjami pomiędzy cyframi a operatorem>>\n')
    for i in string.split(" "):
        lista.append(i)

    if lista[1] == '+':
        print(float(lista[0]) + float(lista[2]))
    elif lista[1] == '-':
        print(float(lista[0]) - float(lista[2]))
    elif lista[1] == '*':
        print(float(lista[0]) * float(lista[2]))
    elif lista[1] == '/':
        print(float(lista[0]) / float(lista[2]))
    elif lista[1] == '^':
        print(float(lista[0]) ** float(lista[2]))