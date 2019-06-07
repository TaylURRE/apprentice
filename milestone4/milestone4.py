import random

from milestone2.merge_sort import merge_sort



def list_generator_1d(min, max, length):
    """
    Generates a list of length `length`,
    with int values between `min` and `max`
    :param min: int
    :param max: int
    :param length: int
    :return: list
    """

    return [random.randint(min, max) for _ in range(length)]


def list_generator_2d(min, max, side):
    """
    Generates a square list of length `side`
    with integer values between `min` and `max`
    :param min: int
    :param max: int
    :param side: int
    :return multi_list: list
    """
    multi_list = []

    for i in range(0, side):
        multi_list.append(list_generator_1d(min, max, side))

    return multi_list

def find_1d_index():
    """
    Look for needle in haystack
    :needle: int
    :haystack: list
    :ni- needle index:
    complexity O(n) | linear complexity
    """
 
    length = 10
    max = length
    min = 0
    needle = random.randint(min, max)
    haystack_1d = list_generator_1d(min, max, length)
    was_found = False
    needle_index = None

    print("Looking for", needle, "in", haystack_1d)

    for ni, needs in enumerate(haystack_1d):
        if needs == needle:
            was_found = True
            needle_index = ni
            print('needle_index:', ni)
            break
    if was_found:
        print("We found the needle in the haystack!")
    else:
        print("We didn't find anything :-(")
    return needle_index


def find_2d_index():
    """
    Look for needle in haystack of haystacks
    :needle: int
    :haystack: list
    :ni- needle index:
    :hi- haystack index:
    complexity O(n^2) | exponential complexity
    """
    max = length
    min = 0
    needle = random.randint(min, max)
    haystack_2d = list_generator_2d(min, max, length)
    was_found = False
    ni = None

    print("Looking for this needle ", needle,
          "in these haystacks", haystack_2d)

    for hi, haystack in enumerate(haystack_2d):
        if not was_found:
            for ni, hay in enumerate(haystack):
                if hay == needle:
                    was_found = True
                    print('needle_index:', ni, 'haystack_index:', hi)
                    break
    if was_found:
        print("We found the needle in the haystack!")
    else:
        print("We didn't find anything :-(")
    return ni


def find_2d_index_pt2(haystack, needle):
    if type(haystack[0]) == list:
        newstack = []
        for stack in haystack:
            newstack.extend(stack)
        haystack = merge_sort(newstack)
    else:
        haystack = merge_sort(haystack)
    print("looking for ", needle, " in haystack ", haystack)
    was_found = False

    def find_index_help(haystack, needle, low, high):
        if high == low:
            return haystack[low] == needle
        mid = (low + high)//2
        if haystack[mid] == needle:
            print('found at', mid)
            was_found = True
            return was_found
        elif haystack[mid] > needle:
            if low == mid:
                return False
            else:
                return find_index_help(haystack, needle, low, mid-1)
        else:
            return find_index_help(haystack, needle, mid+1, high)
    while not was_found:
        if len(haystack) == 0:
            return False
        else:
            return find_index_help(haystack, needle, 0, len(haystack)-1)

def find_result(fun_result):
    was_found = fun_result
    fun_statement = ""
    if was_found:
        fun_statement = "We found the needle in the haystack!"
    else:
        fun_statement = "We didn't find anything :-("
    return fun_statement

min = 0
max = 200
length = 30
needle_2d = random.randint(min, max)
h_2d = list_generator_2d(min, max, length)

print(find_result(find_2d_index_pt2(h_2d, needle_2d)))

