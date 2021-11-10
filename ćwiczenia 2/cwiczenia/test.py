from task_3 import duplicate_and_sort
from task_4 import names_processing
from task_5 import reverse_dict


class TestCLassTask3:
    def test_duplicate_and_sort(self):
        not_sorted_list = [0, -10, 3, 1, 2, -10]
        sorted_list = [-10, 0, 1, 2, 3]
        assert duplicate_and_sort(not_sorted_list) == sorted_list


class TestClassTask4:
    def test_return_bool_empty_string(self):
        name = input()
        assert not name

    def test_names_processing(self):
        list_test = ["john   doe", "AnnE Marie", "JOhn smith"]
        list_done = ["John Doe", "Anne Marie", "John Smith"]

        assert names_processing(list_test) == list_done

class TestClassTask5:
    def test_reverse_dict(self):
        dictionary = {0: 20, 1: 9, 2: 8, 3: 5, 4: 12, 5: 2, 6: 12, 7: 19, 8: 13, 9: 5, 10: 10, 11: 8, 12: 15, 13: 0, 14: 2, 15: 10, 16: 19, 17: 5, 18: 17, 19: 19, 20: 7}
        dictionary_t = {20: 0, 9: 1, 8: 11, 5: 17, 12: 6, 2: 14, 19: 19, 13: 8, 10: 15, 15: 12, 0: 13, 17: 18, 7: 20}
        assert reverse_dict(dictionary) == dictionary_t