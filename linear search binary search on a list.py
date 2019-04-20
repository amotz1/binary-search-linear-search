import math

DEVELOPMENT_MODE = True
# this function takes two arguments, the first one is the list and the second one is an element to find in the list. it loop through the list checking every element if it is the element that i specified and if it is it prints the number is in the list and return TRUE
# if it doesn't find the number it print "the number is not in the list and returns false
def linear_search(list, number_to_search):
    for i in list:
        if i == number_to_search:
            print("the number is in the list and the index in the list is", list.index(number_to_search))
            return True
    print("the number is not in the list")
    return False


# this function takes no arguments. it is making a list_of_numberstosearch variable that is a list of numbers to search that are in the testcase variable. it then loops through the list_of_numberstosearch variable
# using linear_search function to search if each number in the list_of_numberstosearch variable is in thet testcase list.
def test_linear_search():
    testcase = [4, 8, 9]
    list_of_numbers_to_search = [8, 4, 9, 3]
    for number_to_search in range(len(list_of_numbers_to_search)):
        assert (linear_search(testcase, list_of_numbers_to_search[number_to_search]))


test_linear_search()


# making a binary search algorithm on a list, it will have 4 arguments. one is a list the second and third will be the start and end index of the list and the last will be the number to search.
# we will create a mid as start+end/2 and then will check if the mid is the number that we search for, if so we will return True. if our number_to_search is bigger then the middle element we will we will call binary search again with index of mid+1 to end
# if our number_to_serach is smaller then the middle element we will call binary search on start until index of mid-1
# we will also check if end-start==0 and the last number is not the number_to_search as a base case, to be prepared for the case the number is not in thet list, if its not we will return False.
# if the list is empty so to not have an error i included an if statement that returns false

def __binary_search(list, start, end, number_to_search):
    mid = math.floor((start + end) / 2)
    if DEVELOPMENT_MODE:
        assert (list == sorted(list), "Error! binary search should only be used on sorted lists.")
    if end == start and list[mid] != number_to_search:
        print("the number is not in the list", list, number_to_search)
        return False
    if list[mid] == number_to_search:
        print("the number is in the list", list, number_to_search)
        return True
    elif list[mid] < number_to_search:
        return __binary_search(list, mid + 1, end, number_to_search)

    else:
        return __binary_search(list, start, math.floor(mid) - 1, number_to_search)



# this is the public variable. first of all i sort the list with the sort of python and then i use thet privet function of binary search with the sorted_list, start and end-1 parameters. i get a boolean and return it to the function.
def binary_search(list, number_to_search):
    sorted_list = sorted(list)
    return __binary_search(sorted_list, 0, len(sorted_list) - 1, number_to_search)



# using a variable testcase that contains a list i created another variable list_of_numberstosearch that is a list of numberstosearch. i loop through them using binarysearch function to check if they all are True or not
def test_binary_search():
    testcase = [0, 1, 3, 4, 5, 6, 8, 9]
    list_of_numberstosearch = [0, 1, 8, 5, 4, 8, 6, 3, 1, 10]
    for number_to_search in range(len(list_of_numberstosearch)):
        assert (binary_search(testcase, list_of_numberstosearch[number_to_search]))


test_binary_search()
