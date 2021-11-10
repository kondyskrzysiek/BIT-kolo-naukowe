from random import randint


def rand_dict(n):
    return {x: randint(0, 20) for x in range(n)}


def reverse_dict(dictionary):
    return {val: key for key, val in dictionary.items()}

if __name__ == '__main__':
    n = int(input('> '))
    if 0 <= n <= 21:
        dict = rand_dict(n)
    else:
        dict = rand_dict(21)

    print(reverse_dict(dict))
