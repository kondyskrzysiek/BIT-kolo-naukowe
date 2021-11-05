if __name__ == '__main__':
    liczba_user = input('podaj liczbę > ')
    digits_sum = 0

    print('długość liczby : ', len(liczba_user))
    for liczba_digit in liczba_user:
        digits_sum += int(liczba_digit)
    print('suma cyfr : ', digits_sum)