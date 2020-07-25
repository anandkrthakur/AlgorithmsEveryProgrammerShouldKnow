# Function to return majority element present in given list
def majorityElement(A):

    # m stores majority element if present
    m = -1

    # initialize counter i with 0
    i = 0

    # do for each element A[j] of the list
    for j in range(len(A)):

        # if the counter i becomes 0
        if i == 0:

            # set the current candidate to A[j]
            m = A[j]

            # reset the counter to 1
            i = 1

        # else increment the counter if A[j] is current candidate
        elif m == A[j]:
            i = i + 1

        # else decrement the counter if A[j] is not current candidate
        else:
            i = i - 1

    return m


if __name__ == '__main__':

    # Assumption - valid input (majority element is present)
    A = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]

    print("Majority element is", majorityElement(A))
