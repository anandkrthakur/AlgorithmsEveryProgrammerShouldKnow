# Find out if a key x exists in the sorted list A
# or not using binary search algorithm
def binarySearch(A, x):

    # search space is A[left..right]
    (left, right) = (0, len(A) - 1)

    # till search space consists of at-least one element
    while left <= right:

        # we find the mid value in the search space and
        # compares it with key value

        mid = (left + right) // 2

        # overflow can happen. Use:
        # mid = left + (right - left) / 2
        # mid = right - (right - left) // 2

        # key value is found
        if x == A[mid]:
            return mid

        # discard all elements in the right search space
        # including the mid element
        elif x < A[mid]:
            right = mid - 1

        # discard all elements in the left search space
        # including the mid element
        else:
            left = mid + 1

    # x doesn't exist in the list
    return -1


if __name__ == '__main__':

    A = [2, 5, 6, 8, 9, 10]
    key = 5

    index = binarySearch(A, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")
