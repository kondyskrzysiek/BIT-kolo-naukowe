from nltk.corpus import stopwords
from string import punctuation
from collections import Counter
from nltk.stem.porter import PorterStemmer
# from nltk.tokenize import sent_tokenize, word_tokenize
# import string

def get_bag_of_words(text):
    words = []
    stop_words = set(stopwords.words("english"))
    for word in text.split('.'):
        words_split = word.split()
        for word_fin in words_split:
            if word_fin not in stop_words and len(word_fin) >=3:
                words.append(word_fin.lower())
    punctuations = set(punctuation)
    words = [word for word in words if word not in punctuations]
    words = [word.strip() for word in words]
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]

    return Counter(words)

# def get_bag_of_words1(text):
#     # partition into sentences and words
#     sentences = sent_tokenize(text)
#     words = []
#     for sentence in sentences:
#         sentence_words = word_tokenize(sentence)
#         words.extend(sentence_words)
#
#     # change to lowercase
#     words = [word.lower() for word in words]
#
#     # remove stop words
#     stop_words = set(stopwords.words("english"))
#     words = [word for word in words if word not in stop_words]
#
#     # remove punctuation
#     punctuations = set(string.punctuation)
#     punctuations.add("...")
#     words = [word for word in words if word not in punctuations]
#
#     # change words to their stems
#     stemmer = PorterStemmer()
#     words = [stemmer.stem(word) for word in words]
#
#     # remove too short stems
#     words = [word for word in words if len(word) >= 3]
#     return Counter(words)




if __name__ == '__main__':
    with open('task2_popular_words.txt') as file:
        text = file.read()
    print(get_bag_of_words(text))
