import openfile as openfile
import os
import task_1
import task_2
import task_3
import task_4

class TestClassTask1:
    def test_get_top_k_words(self):
        k = 3
        text = 'tak nie tak nie tak ja nie tak lub lub'
        popular_words = task_1.get_top_k_words(text, k)
        popular_words_finish = ['tak','nie','lub']

        assert popular_words_finish == popular_words

class TestClassTask2:
    def test_get_top_k_words_in_file(self):
        path = 'task2_popular_words.txt'
        k =5
        popular_word = task_2.get_top_k_words_in_file(path,k)

        test_popular_word = [('do', 9), ('on', 6), ('he', 6), ('so', 5), ('out', 5)]

        assert test_popular_word == popular_word

class TestClassTask3:
    def test_read_text_files(self):
        dir_path = 'texts_task_3'
        text = []

        assert task_3.read_text_files(dir_path) == text

    def test_empty_file(self):
        test = ''
        filepath = os.path.join('texts_task_3','text3.txt')
        with open(filepath) as file:
            text =  file.read()
            text = text.strip()

        assert text == test

class TestClassTask4:
    def test_string_of_read_test(self):

        with open('task2_popular_words.txt') as file:
            text = file.read()
        assert type(text) == str

    def test_string_lower(self):
        string = ' Ambre\n'
        string.strip()
        string_t = 'ambre'

        assert string.lower() == string_t

    def test_words(self):
        word_dict = {}
        with open('task2_popular_words.txt') as file:
            text = file.read()
        words_list = task_4.get_bag_of_words(text)
        for word in words_list:
            word_dict[word] = word_dict.get(word,0) + 1


        assert task_4.Counter(words_list) == word_dict
