# Utility function to swap values at two indices in the list
def swap(A, i, j):

    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Function to perform selection sort on list
def selectionSort(A):

    for i in range(len(A) - 1):

        # find the minimum element in the unsorted sublist[i..n-1]
        # and swap it with A[i]
        min = i

        for j in range(i + 1, len(A)):
            # if A[j] element is less, then it is the minimum
            if A[j] < A[min]:
                min = j  # update index of min element

        # swap the minimum element in sublist[i..n-1] with A[i]
        swap(A, min, i)


if __name__ == '__main__':

    A = [3, 5, 8, 4, 1, 9, -2]

    selectionSort(A)

    # print the sorted list
    print(A)
