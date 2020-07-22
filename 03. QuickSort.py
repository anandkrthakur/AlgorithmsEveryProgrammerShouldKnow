def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Partition using Lomuto partition scheme
def partition(a, start, end):

    # Pick rightmost element as pivot from the list
    pivot = a[end]

    # elements less than pivot will be pushed to the left of pIndex
    # elements more than pivot will be pushed to the right of pIndex
    # equal elements can go either way
    pIndex = start

    # each time we finds an element less than or equal to pivot,
    # pIndex is incremented and that element would be placed
    # before the pivot.
    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, pIndex)
            pIndex = pIndex + 1

    # swap pIndex with Pivot
    swap(a, end, pIndex)

    # return pIndex (index of pivot element)
    return pIndex


# Quicksort routine
def quicksort(a, start, end):

    # base condition
    if start >= end:
        return

    # rearrange the elements across pivot
    pivot = partition(a, start, end)

    # recur on sublist containing elements less than pivot
    quicksort(a, start, pivot - 1)

    # recur on sublist containing elements more than pivot
    quicksort(a, pivot + 1, end)


# Python implementation of quicksort algorithm
if __name__ == '__main__':

    a = [9, -3, 5, 2, 6, 8, -6, 1, 3]

    quicksort(a, 0, len(a) - 1)

    # print the sorted list
    print(a)
