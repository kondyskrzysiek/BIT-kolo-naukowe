#ciąg fibonnaciego
#imperatywnie
# def fibonnaciego(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         print(a)
#         a,b = b,a+b
#
# if __name__ == '__main__':
#     fibonnaciego(10)

#funkcyjnie
def fibonnaciego(n):
    if n<=1:
        return n
    else:
        # print(fibonnaciego(n-2) + fibonnaciego(n-1))
        return fibonnaciego(n-2) + fibonnaciego(n-1)

if __name__ == '__main__':
    for i in range(10):
        print(fibonnaciego(i))