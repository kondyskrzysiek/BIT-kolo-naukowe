from random import randint

def duplicate_and_sort(lista):
    return sorted(set(lista))

if __name__ == '__main__':
    numbers = [randint(-10,10) for _ in range(100)]
    numbers = duplicate_and_sort(numbers)
    print(numbers)