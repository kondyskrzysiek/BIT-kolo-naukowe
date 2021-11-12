from operator import itemgetter

def get_text_statictics(text, k):
    words = text.split()
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1

    counter = list(counter.items())
    counter.sort(key=itemgetter(1),reverse=True)
    return counter[:k] , len(words)

if __name__ == '__main__':
    k = 3
    text = input("> ")
    # text = 'la la la la la lnie lnie nie nei nie nie nie nie nie nie nie tak t wiefjo wijweo jwef oijewf'
    words , len_words = get_text_statictics(text, k)
    for word , number in words:
        print(f'słowo >>{word}<< wystepuje raz na  {round(len_words/number,2)} słów')