import math


def merge_it(left, right):
    """"
    Iterates through the left and right side of the list items then compares
    The lower list item is appended to a new list(sorted_list)
    When the while loop no longer applies append the leftover list items
    On the left and right list slicing at the list index

    :params left and right of (list) li[left index] ri[right index]
    :return sorted_list

    """""

    li = 0
    ri = 0
    sorted_list = []
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            sorted_list.append(left[li])
            li += 1
        else:
            sorted_list.append(right[ri])
            ri += 1

    sorted_list += left[li:]
    sorted_list += right[ri:]
    return sorted_list


def merge_sort(items):
    """
    Uses merge sort algorithm to sort items
    From input list and return new list in sorted order

    Base case: If the length of the items list is less than or equal to 1
    returns the list

    Takes items list and splits it in half
    Two lists created left and right side
    Recursion: Left and Right side are run through the merge_sort
    Merges left and right side by comparing numbers at indices
    See merge_it(left,right)

    :param items: list of comparable items type integer, e.g. [3, 1, 2]
    :return: a sorted list containing every item from the input list
    """
    if len(items) <= 1:
        return(items)
    middle = math.floor(len(items)/2)
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    return(merge_it(left, right))
