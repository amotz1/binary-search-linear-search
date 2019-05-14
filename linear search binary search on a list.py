import math

DEVELOPMENT_MODE = True


# search elements in a list returns the index of the element if found and returns -1 if not found
def linear_search(list, number_to_search):
    count = 0
    for i in list:
        if i == number_to_search:
            return count
        count = count + 1
    return -1


def test_linear_search():
    test_case = [0, 8, 9, 4]
    list_of_numbers_to_search = [8, 4, 9, 0]
    for number_to_search in list_of_numbers_to_search:
        assert linear_search(test_case, number_to_search) == test_case.index(number_to_search)
        assert linear_search(test_case, 10) == -1


test_linear_search()


# this is a helper function that perform binary search on a limited range in a list

def __binary_search(list, start, end, number_to_search):
    mid = math.floor((start + end) / 2)
    if end == start and list[mid] != number_to_search:
        return -1
    elif list[mid] == number_to_search:
        return mid
    elif list[mid] < number_to_search:
        return __binary_search(list, mid + 1, end, number_to_search)
    else:
        return __binary_search(list, start, math.floor(mid) - 1, number_to_search)
    assert False


# this is the public function. it gets a sorted list and it then use the binary_search function with it and the arguments 0 to len(sorted_list)-1.


def binary_search(sorted_list, number_to_search):
    if DEVELOPMENT_MODE:
        assert sorted_list == sorted(sorted_list), "Error! binary search should only be used on sorted lists."
    return __binary_search(sorted_list, 0, len(sorted_list) - 1, number_to_search)


def test_binary_search():
    test_case = [0, 1, 3, 4, 5, 6, 8, 9]
    list_of_numbers_to_search = [0, 1, 8, 5, 4, 8, 6, 3, 1]
    for number_to_search in list_of_numbers_to_search:
        assert binary_search(test_case, number_to_search) == test_case.index(number_to_search)
    assert binary_search(test_case, 10) == -1


test_binary_search()


#TODO(yotam): i still am a little bit bewildered here as you saw in the comment
def yotam_test():
    list = [0, 1, 2]
    if linear_search(list, 0):
        print("found 0")
    else:
        print(linear_search(list, 0))
        print("not found 0")


yotam_test()
