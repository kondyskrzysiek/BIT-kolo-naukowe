from math import sqrt

def wzor_herona(a,b,c) -> float:
    s = 0.5*(a+b+c)
    A = sqrt(s*(s-a)*(s-b)*(s-c))
    return round(A,3)

# class TestClass:
#     def test_wzor_herona(self):
#         assert wzor_herona(4.0,5.0,7.0) == 9.798

if __name__ == "__main__":
    a = float(input('podaj bok trójkąta: '))
    b = float(input('podaj bok trójkąta: '))
    c = float(input('podaj bok trójkąta: '))

    if a<b+c and b<a+c and c<a+b:
        print(wzor_herona(a,b,c))
    else:
        print('podane cyfry nie utworzą trójkąt')