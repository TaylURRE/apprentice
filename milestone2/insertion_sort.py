def insertion_sort(items):
    for i in range(1, len(items)):
        val = items[i]
        position = i

        while position > 0 and items[position - 1] > val:
            items[position] = items[position - 1]
            position -= 1

        items[position] = val

    return items
