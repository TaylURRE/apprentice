from random import randint
from time import time

from milestone2.merge_sort import merge_sort
from milestone2.insertion_sort import insertion_sort

sort_functions = {
    'merge_sort': merge_sort,
    'insertion_sort': insertion_sort
}


def benchmark(sort_fns, list_length, num_passes):
    """
    For each sorting function provided, generate a list
    with the specified length, then
    track the time to sort it.
    Repeat the specified number of times, then return the average
    run time for each sorting function.

    Because lists with shorter lengths can be sorted extremely
    quickly on modern hardware,it is helpful to take the average
    of many run times to avoid noisiness in the data.

    :param sort_fns: dictionary of sorting functions
    :param list_length: length of the list to generate that will
    be passed to sorting functions
    :param num_passes: number of times to run each sorting function
    :return: dictionary of sorting function name to average
    run time for given list length
    """
    times = {}

    for fn, sort_fn in sort_fns.items():
        times[fn] = 0

    for _ in range(num_passes):
        items = generate_list(list_length)
        for fn, sort_fn in sort_fns.items():
            items_copy = list(items)
            start = time()
            sort_fn(items_copy)
            end = time()
            duration = (end - start)
            times[fn] += (duration / num_passes)

    return times


def generate_list(length):
    """
    Generates a list of random integers between 0 and 100,000 to help with our
    benchmarking.

    :param length: length of list to be returned
    :return: list of random integers between 0 and 100,000
    """

    rand_list = [randint(0, 100000) for i in range(length)]

    return(rand_list)


if __name__ == '__main__':
    list_length = 10
    num_passes = 10000

    while num_passes >= 10:
        results = benchmark(sort_functions, list_length, num_passes)

        print('Time to sort list length %s:\n%s\n' % (list_length, results))

        list_length = list_length * 10
        num_passes = int(num_passes / 10)
