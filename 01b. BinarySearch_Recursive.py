# Find out if a key x exists in the sorted list
# A[left..right] or not using binary search algorithm
def binarySearch(A, left, right, x):

    # Base condition (search space is exhausted)
    if left > right:
        return -1

    # we find the mid value in the search space and
    # compares it with key value

    mid = (left + right) // 2

    # overflow can happen. Use below
    # mid = left + (right - left) / 2

    # Base condition (key value is found)
    if x == A[mid]:
        return mid

    # discard all elements in the right search space
    # including the mid element
    elif x < A[mid]:
        return binarySearch(A, left, mid - 1, x)

    # discard all elements in the left search space
    # including the mid element
    else:
        return binarySearch(A, mid + 1, right, x)


if __name__ == '__main__':

    A = [2, 5, 6, 8, 9, 10]
    key = 5

    (left, right) = (0, len(A) - 1)
    index = binarySearch(A, left, right, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")
