# Data structure for Max Heap
# return left child of A[i]
def LEFT(i):
    return 2 * i + 1


# return right child of A[i]
def RIGHT(i):
    return 2 * i + 2


# Utility function to swap two indices in the list
def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Recursive Heapify-down algorithm. The node at index i and
# its two direct children violates the heap property
def Heapify(A, i, size):

    # get left and right child of node at index i
    left = LEFT(i)
    right = RIGHT(i)

    largest = i

    # compare A[i] with its left and right child
    # and find largest value
    if left < size and A[left] > A[i]:
        largest = left

    if right < size and A[right] > A[largest]:
        largest = right

    # swap with child having greater value and
    # call heapify-down on the child
    if largest != i:
        swap(A, i, largest)
        Heapify(A, largest, size)


# function to remove element with highest priority (present at root)
def pop(A, size):

    # if heap has no elements
    if size <= 0:
        return -1

    top = A[0]

    # replace the root of the heap with the last element
    # of the list
    A[0] = A[size - 1]

    # call heapify-down on root node
    Heapify(A, 0, size - 1)

    return top


# Function to perform heapsort on list A of size n
def heapSort(A):

    # build a priority queue and initialize it by given list
    n = len(A)

    # Build-heap: Call heapify starting from last internal
    # node all the way upto the root node
    i = (n - 2) // 2
    while i >= 0:
        Heapify(A, i, n)
        i = i - 1

    # pop repeatedly from the heap till it becomes empty
    while n:
        A[n - 1] = pop(A, n)
        n = n - 1


if __name__ == '__main__':

    A = [6, 4, 7, 1, 9, -2]

    # perform heapsort on the list
    heapSort(A)

    # print the sorted list
    print(A)
