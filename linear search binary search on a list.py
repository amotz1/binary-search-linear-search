import math


# this function takes two arguments, the first one is the list and the second one is an element to find in the list it loop through the list  checking every element if it is the element that i specified and if it is it prints sucesss and return TRUE
# if it doesn't find the number it print "the number is not in the list and returns false
def linear_search(list, number_tosearch):
    for i in range(len(list)):
        if list[i] == number_tosearch:
            print("the number is in the list")
            return True
    print("the number is not in the list")
    return False


# this function takes no arguments. it is making a list_of_numberstosearch variable that is a list of numbers most of them in the testcase bariable but one of them is not. it then loops through the list_of_numberstosearch variable
# using linear_search function to search if each number in the list_of_numberstosearch variable is in thet testcase list.
def test_linear_search():
    testcase = [4, 8, 9]
    list_of_numberstosearch = [8, 4, 9]
    for number_tosearch in range(len(list_of_numberstosearch)):
        assert (linear_search(testcase, list_of_numberstosearch[number_tosearch]))


test_linear_search()


# making a binary search algorithm on a list, it will have 4 arguments. one is a list the second and third will be the start and end index of the list and the last will be the number to search.
# we will create a mid as start+end/2 and then will check if the mid is the number that we search for, if so we will return True. if our numbertosearch is bigger then the middle element we will we will call binary search again with index of mid+1 to end
# if our numberto serach is smaller then the middle element we will call binary search on start until index of mid-1
# we will also check if end-start<=1 and the element in the mid position is equal ro numbertosearch. if so we will return True and if not we will return False
# if there are no elements in the list number_to_search is not in the list for sure so we return False

def __binary_search(list, start, end, number_to_search):
    mid = (start + end) / 2
    if start - end == 0 and list[math.floor(mid)] != number_to_search:
        print("the number is not in the list", list, number_to_search)
        return False
    if list[math.floor(mid)] == number_to_search:
        print("the number is in the list", list, number_to_search)
        return True
    elif list[math.floor(mid)] < number_to_search:
        boolean = __binary_search(list, math.floor(mid) + 1, end, number_to_search)
        return boolean
    else:
        boolean1 = __binary_search(list, start, math.floor(mid) - 1, number_to_search)
        return boolean1


def binary_search(list, number_to_search):
    sorted_list = sorted(list)
    boolean = __binary_search(sorted_list, 0, len(sorted_list) - 1, number_to_search)
    return boolean


def test_binary_search():
    testcase = [1, 3, 6, 8, 4, 5, 8, 9, 0, 2, 6]
    list_of_numberstosearch = [2, 0,  9, 8, 5, 4, 8, 6, 3, 1]
    for number_tosearch in range(len(list_of_numberstosearch)):
        assert (binary_search(testcase, list_of_numberstosearch[number_tosearch]))


test_binary_search()
