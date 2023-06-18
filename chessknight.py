# This is a python solution for the chess knight algorithm:
# Given a 8x8 game board, make a program were given the starting square and the target square
# it calculates the minimum number of chess knight moves it takes to go from the start to the target.
#
# Game Board:
# |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
# |  8 |  9 | 10 | 11 | 12 | 13 | 14 | 15 |
# | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 |
# | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
# | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |
# | 40 | 41 | 42 | 43 | 44 | 45 | 46 | 47 |
# | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
# | 56 | 57 | 58 | 59 | 60 | 61 | 62 | 63 |

# Example 1:
# start = 0; target = 1
# minimum number of moves: 3
#
# Example 2:
# start: 19; target = 36
# minimum number of moves: 1

#-----------------------------------------
# This solution utilizes Breadth-First Search:
# Given the starting square, we check all legal knight moves
# that can be made. If we do not reach the destination,
# we enqueue all the legal moves. We repeat the process of checking
# all legal moves from the queued positions until we reach the
# target square. 
# -----------------------------------------
# Given the starting square and the target square 
# returns the minimum number of knight moves
# to reach target square from start square.
def knight(start, target):
   # Representing the game board as a dictionary
    board = {}
    num = 0
    
    # Mapping the square number to a coordinate pair
    # For example: 0 -> [0,0] ; 1 -> [0,1] ...
    # ... 62 -> [7,6] ; 63 -> [7,7]
    while (num < 64):
        for i in range(8):
            for j in range(8):
                board[num] = [i, j] # [row, col]
                num += 1

     # all possible movements for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []
    # Pushing the starting position into the queue
    queue.append(board[start][0])
    queue.append(board[start][1])
    queue.append(0)
    # queue = [start_x, start_y, distance = 0]
    
    # A 8x8 matrix that marks which squares on the board have been visited.
    # Starting by setting all of the squares to False(not visited)
    visited = [[False for i in range(8)] for j in range(8)]
    # Start square is set to True
    visited[board[start][0]][board[start][1]] = True

    # Loop while the queue is not empty
    while (len(queue) > 0):
        # Pop the next element in queue
        x = queue.pop(0)
        y = queue.pop(0)
        dist = queue.pop(0)
        
        # return the distance if we reach the destination square
        if (x == board[target][0] and y == board[target][1]):
            return dist

        # Make all legal knight moves
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            # Check that the moves are inside the board.
            # If they are, push into the queue.
            if (nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append(nx)
                queue.append(ny)
                queue.append(dist + 1)


# Checking knight(), with start = 19, target = 36
print(knight(19, 36)) # Prints out "1".

# Checking knight(), with start = 0, target = 1
print(knight(0, 1)) # Prints out "3".
