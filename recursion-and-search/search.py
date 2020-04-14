#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)
    # IF LIST[INDEX] == target:
    # return Index
    # if index == len(list):
    #     return None
    # else:
    #     return 

def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # index has to be greater than the length of the entire array reduced by 1
    if index > (len(array) - 1):
        return None
    # item is where its' index is
    if item == array[index]:
        return index
    else:
        return linear_search_recursive(array, item, index+1)
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item, 0, len(array)-1)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    min = 0
    max = len(array) - 1
    while min <= max:
        midpoint = (min + max)
        if array[midpoint] == item:
            return midpoint
        elif array[midpoint] < item:
            min = midpoint + 1
        else:
            max = midpoint - 1
        
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1
    if left <= right:
        midpoint = (left + right) // 2
        if array[midpoint] == item:
            return midpoint
        if array[midpoint] < item:
            return binary_search_recursive(array, item, midpoint+1, right)
        elif array[midpoint] > item:
            return binary_search_recursive(array[:midpoint], item, left, midpoint-1)
    return None
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
