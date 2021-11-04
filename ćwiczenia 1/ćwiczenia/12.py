from random import randint

def reczneOdwracanie(lista):
    lista_odwrocona = []
    for i in range(9,-1,-1):
        lista_odwrocona.append(lista[i])
    return lista_odwrocona

def pythonoweOdwracanie(lista):
    reverse_lista =[]
    reverse_lista = lista[::-1]
    return reverse_lista

if __name__ == "__main__":
    lista = [randint(0,10) for _ in range(10)]

    print('lista nie odwrócona ',lista)
    print('recznie odwrócone: ', reczneOdwracanie(lista))
    print('pythonowo odwrócone: ', pythonoweOdwracanie(lista))