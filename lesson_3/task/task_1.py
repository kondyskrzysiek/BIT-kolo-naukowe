from operator import itemgetter

def get_top_k_words(text, k):
    words_dict = {}
    counter = [word for word in text.split()]
    for word in counter:
        words_dict[word] = words_dict.get(word,0) + 1
    counter = list(words_dict.items())
    counter.sort(key=itemgetter(1),reverse=True)
    counter = [key for key,value in counter]

    return counter[:k]

if __name__ == '__main__':
    k = 3
    text = input('> ')
    popular_word = get_top_k_words(text,k)
    print(popular_word)