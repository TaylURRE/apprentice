def run_heap_sort(hlist):
    hlist = hlist

    def heap(hsize, largest):
        # root of tree largest number
        i = largest

        # index of the left child left(i)
        left = (2 * i)

        # index of the right child right(i)
        right = (2 * i) + 1

        if left < hsize and hlist[left] > hlist[i]:
            largest = left
        if right < hsize and hlist[right] > hlist[largest]:
            largest = right
        if largest != i:
            swap(i, largest)
            heap(hsize, largest)

    def heap_sort():
        end = len(hlist)
        # index of the first number parent(i)
        # parent = i//2
        start = end // 2

        for i in range(start, -1, -1):
            swap(i, 0)
            heap(end, i)
        for i in range(end - 1, 0, 1):
            swap(i, 0)
            heap(i, 0)

        return hlist

    def swap(small, large):
        hlist[small], hlist[large] = hlist[large], hlist[small]
    heap_sort()
    return hlist
