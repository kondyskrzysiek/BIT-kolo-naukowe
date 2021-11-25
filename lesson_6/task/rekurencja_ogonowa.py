import itertools


def s(N, akum):
    if N == 0:
        return akum
    else:
        return s(N - 1, N * akum)


def silnia(N: int):
    return s(N, 1)


def silnia1(N: int):
    if N == 0:
        return 1
    else:
        return N * silnia1(N - 1)


if __name__ == "__main__":
    n = 0
    try:
        for i in itertools.count(1):
            silnia1(i)
            n = i
    except:
        print(n)
        print('wielkość liczby silnia = ', len(str(silnia1(n))))
