import math

DEVELOPMENT_MODE = True


# this function takes two arguments, the first one is the list and the second one is an element to find in the list.
# it loop through the list checking every element if it is the element that i specified and if it is the element it returns the index of that number in the list.
# it doesn't find the number it returns false


def linear_search(list, number_to_search):
    for i in list:
        if i == number_to_search:
            return list.index(number_to_search)
    return False


# this function takes no arguments. it is making a list_of_numbers_to_search variable that is a list of numbers to search that are in the testcase variable.
# it then loops through the list_of_numberstosearch variable
# using linear_search function to search if each number in the list_of_numberstosearch variable is in the testcase list.
# it also checks if the number 3 is not in the list now
def test_linear_search():
    test_case = [4, 8, 9]
    list_of_numbers_to_search = [8, 4, 9]
    for number_to_search in list_of_numbers_to_search:
        assert linear_search(test_case, number_to_search) == test_case.index(number_to_search)
    assert linear_search(test_case, 3) == False


test_linear_search()


# making a binary search algorithm on a list, it will have 4 arguments. one is a list the second and third will be the start and end index of the list and the last will be the number to search.
# we will create a mid as start+end/2 and then will check if the mid is the number that we search for, if so we will return True.
# if our number_to_search is bigger then the middle element we will we will call binary search again with index of mid+1 to end
# if our number_to_serach is smaller then the middle element we will call binary search on start until index of mid-1
# we will also check if end == start and the last number is not the number_to_search as a base case, to be prepared for the case the number is not in thet list, if its not we will return False.


def __binary_search(list, start, end, number_to_search):
    mid = math.floor((start + end) / 2)
    if end == start and list[mid] != number_to_search:
        return False
    elif list[mid] == number_to_search:
        return True
    elif list[mid] < number_to_search:
        return __binary_search(list, mid + 1, end, number_to_search)

    else:
        return __binary_search(list, start, math.floor(mid) - 1, number_to_search)
    assert False


# this is the public function. it gets a sorted list and it then use the __binary_search function with it and the arguments 0 to len(sorted_list)-1.
def binary_search(sorted_list, number_to_search):
    if DEVELOPMENT_MODE:
        assert sorted_list == sorted(sorted_list), "Error! binary search should only be used on sorted lists."
    return __binary_search(sorted_list, 0, len(sorted_list) - 1, number_to_search)


# using a variable test_case that contains a list i created another variable list_of_numbers_to_search that is a list of numbers to search.
# i loop through them using binarysearch function to check if they all are True or not
# i also added assert to check that the number 10 is not in the list
def test_binary_search():
    test_case = [0, 1, 3, 4, 5, 6, 8, 9]
    list_of_numbers_to_search = [0, 1, 8, 5, 4, 8, 6, 3, 1]
    for number_to_search in list_of_numbers_to_search:
        assert (binary_search(test_case, number_to_search))
    assert binary_search(test_case, 10) == False


test_binary_search()
