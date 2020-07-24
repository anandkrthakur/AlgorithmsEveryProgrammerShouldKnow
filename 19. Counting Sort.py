"""
    list -- the input list of integers to be sorted
    k -- a number such that all integers are in the range 0..k-1
"""

def countSort(A, k):

    # create an integer list of size n to store sorted list
    output = [0] * len(A)

    # create an integer list of size k, initialized by all zero
    freq = [0] * k

    # using value of integer in the input list as index,
    # store count of each integer in freq list
    for i in A:
        freq[i] = freq[i] + 1

    # calculate the starting index for each integer
    total = 0
    for i in range(k):
        oldCount = freq[i]
        freq[i] = total
        total += oldCount

    # copy to output list, preserving order of inputs with equal keys
    for i in A:
        output[freq[i]] = i
        freq[i] = freq[i] + 1

    # copy the output list back to the input list
    for i in range(len(A)):
        A[i] = output[i]


if __name__ == '__main__':

    A = [4, 2, 10, 10, 1, 4, 2, 1, 10]

    # range of list elements
    k = 11

    countSort(A, k)
    print(A)
