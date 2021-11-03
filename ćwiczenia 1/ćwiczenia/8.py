if __name__ == "__main__":
    a = int(input('budget: '))
    x = 'x'
    y = 1
    while y <= a:
        print(x)
        x += 'xx'
        y += len(x)