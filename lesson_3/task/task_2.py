from operator import itemgetter

def get_top_k_words(text, k):
    words_dict = {}
    counter = [word for word in text.split()]
    for word in counter:
        words_dict[word] = words_dict.get(word,0) + 1
    counter = list(words_dict.items())
    counter.sort(key=itemgetter(1),reverse=True)

    return counter[:k]

if __name__ == '__main__':
    k = 3
    while True:
        filepath = input('file path :> ')
        try:
            with open(filepath) as file:
                text = file.read()
            break
        except FileNotFoundError:
            print('not found file ')

    while True:
        try:
            k = int(input('number top popular words in text :> '))
            break
        except ValueError as v:
            print('Requires number! Got error: ',v)

    popular_word = get_top_k_words(text,k)
    print(popular_word)