if __name__ == '__main__':
    for i in range(1,101):
        if i % 3 == 0 and i % 5== 0:
            print("FizzBuzz",'\t',end='')
        elif i % 5 ==0:
            print("Buzz",'\t',end='')
        elif i % 3 == 0:
            print('Fizz','\t',end='')
        else:
            print(i,'\t',end='')