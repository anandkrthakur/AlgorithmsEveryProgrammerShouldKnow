# Function to find contiguous sublist with the largest sum
# in given set of integers
def kadane(A):

    # find maximum element present in given list
    maximum = max(A)

    # if list contains all negative values, return maximum element
    if maximum < 0:
        return maximum

    # stores maximum sum sublist found so far
    maxSoFar = 0

    # stores maximum sum of sublist ending at current position
    maxEndingHere = 0

    # do for each element of the given list
    for i in A:

        # update maximum sum of sublist "ending" at index i (by adding
        # current element to maximum sum ending at previous index i-1)
        maxEndingHere = maxEndingHere + i

        # if maximum sum is negative, set it to 0 (which represents
        # an empty sublist)
        maxEndingHere = maximum(maxEndingHere, 0)

        # update result if current sublist sum is found to be greater
        maxSoFar = maximum(maxSoFar, maxEndingHere)

    return maxSoFar


if __name__ == '__main__':

    A = [-8, -3, -6, -2, -5, -4]
    print("The sum of contiguous sublist with the largest sum is", kadane(A))
