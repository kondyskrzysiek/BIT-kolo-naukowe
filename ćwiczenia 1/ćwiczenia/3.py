def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def mnozenie(a,b):
    return a*b

def dzielenie(a,b):
    return a/b

def potęgowanie(a,b):
    return a**b

if __name__ == "__main__":
    a = int(input("a: "))
    operation = input('operation: +,-,*,/,^ :   ')
    b = int(input("b: "))
    if operation == '+':
        print(dodawanie(a,b))
    elif operation == '-':
        print(odejmowanie(a,b))
    elif operation == '*':
        print(mnozenie(a,b))
    elif operation == '/':
        print(dzielenie(a,b))
    elif operation == '^':
        print(potęgowanie(a,b))