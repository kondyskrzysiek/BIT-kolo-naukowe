from task_3 import duplicate_and_sort

def test_duplicate_and_sort():
    not_sorted_list = [0,-10,3,1,2,-10]
    sorted_list = [-10,0,1,2,3]
    assert duplicate_and_sort(not_sorted_list) == sorted_list
