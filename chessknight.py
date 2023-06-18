def solution(src, dest):
    board = {}
    num = 0

    while (num < 64):
        for i in range(8):
            for j in range(8):
                board[num] = [i, j] # [row, col]
                num += 1

     # all possible movements for the knight
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    queue = []
    queue.append(board[src][0])
    queue.append(board[src][1])
    queue.append(0)

    visited = [[False for i in range(8)] for j in range(8)]
    visited[board[src][0]][board[src][1]] = True
    
    while (len(queue) > 0):
        x = queue.pop(0)
        y = queue.pop(0)
        dist = queue.pop(0)

        if (x == board[dest][0] and y == board[dest][1]):
            return dist

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append(nx)
                queue.append(ny)
                queue.append(dist + 1)
        
    
print(solution(19, 36))


    