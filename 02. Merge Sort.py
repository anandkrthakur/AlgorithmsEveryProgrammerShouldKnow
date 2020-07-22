# Merge two sorted sub-lists A[low .. mid] and A[mid + 1 .. high]
def merge(A, aux, low, mid, high):

    k = low
    i = low
    j = mid + 1

    # While there are elements in the left and right runs
    while i <= mid and j <= high:

        if A[i] <= A[j]:
            aux[k] = A[i]
            k = k + 1
            i = i + 1
        else:
            aux[k] = A[j]
            k = k + 1
            j = j + 1

    # Copy remaining elements
    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1

    # No need to copy the second half

    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        A[i] = aux[i]


# Sort list A [low..high] using auxiliary list aux
def mergeSort(A, aux, low, high):

    # Base case
    if high == low:     # if run size == 1
        return

    # find mid point
    mid = (low + ((high - low) >> 1))

    # recursively split runs into two halves until run size == 1,
    # then merge them and return back up the call chain

    mergeSort(A, aux, low, mid)         # split / merge left  half
    mergeSort(A, aux, mid + 1, high)    # split / merge right half

    merge(A, aux, low, mid, high)       # merge the two half runs


# Function to check if A is sorted in ascending order or not
def isSorted(A):

    prev = A[0]
    for i in range(1, len(A)):
        if prev > A[i]:
            print("MergeSort Fails!!")
            return False

        prev = A[i]

    return True


# Implementation of Merge Sort Algorithm in Python
if __name__ == '__main__':

    A = [12, 3, 18, 24, 0, 5, -2]
    aux = A.copy()

    # sort list 'A' using auxiliary list 'aux'
    mergeSort(A, aux, 0, len(A) - 1)

    if isSorted(A):
        print(A)
