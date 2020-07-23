from collections import deque


# Below lists details all 8 possible movements
row = [-1, -1, -1, 0, 0, 1, 1, 1]
col = [-1, 0, 1, -1, 1, -1, 0, 1]


# check if it is possible to go to pixel (x, y) from
# current pixel. The function returns false if the pixel
# has different color or it is not a valid pixel
def isSafe(M, x, y, target):
    return 0 <= x < len(M) and 0 <= y < len(M[0]) and M[x][y] == target


# Flood fill using BFS
def floodfill(M, x, y, replacement):

    # create a queue and enqueue starting pixel
    q = deque()
    q.append((x, y))

    # get target color
    target = M[x][y]

    # run till queue is not empty
    while q:

        # pop front node from queue and process it
        x, y = q.popleft()

        # replace current pixel color with that of replacement
        M[x][y] = replacement

        # process all 8 adjacent pixels of current pixel and
        # enqueue each valid pixel
        for k in range(len(row)):
            # if adjacent pixel at position (x + row[k], y + col[k]) is
            # a valid pixel and have same color as that of current pixel
            if isSafe(M, x + row[k], y + col[k], target):
                # enqueue adjacent pixel
                q.append((x + row[k], y + col[k]))


if __name__ == '__main__':

    # matrix showing portion of the screen having different colors
    M = [
            ['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
            ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
            ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
            ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
            ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
            ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
            ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
            ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

    # start node
    x = 3
    y = 9

    # target color = "X"
    # replacement color
    replacement = 'C'

    # replace target color with replacement color
    floodfill(M, x, y, replacement)

    # print the colors after replacement
    for r in M:
        print(r)
