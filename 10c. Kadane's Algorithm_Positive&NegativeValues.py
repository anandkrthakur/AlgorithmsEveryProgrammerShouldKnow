# Function to find contiguous sublist with the largest sum
# in given set of integers (handles negative numbers as well)
def kadaneNeg(A):

    # stores maximum sum sublist found so far
    maxSoFar = A[0]

    # stores maximum sum of sublist ending at current position
    maxEndingHere = A[0]

    # traverse the given list
    for i in range(1, len(A)):

        # update maximum sum of sublist "ending" at index i (by adding
        # current element to maximum sum ending at previous index i-1)
        maxEndingHere = maxEndingHere + A[i]

        # maximum sum is should be more than the current element
        maxEndingHere = max(maxEndingHere, A[i])

        # update result if current sublist sum is found to be greater
        maxSoFar = max(maxSoFar, maxEndingHere)

    return maxSoFar


if __name__ == '__main__':

    A = [-8, -3, -6, -2, -5, -4]

    print("The sum of contiguous sublist with the largest sum is", kadaneNeg(A))
