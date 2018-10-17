def waterInjection(matrix, r, c):

    m = len(matrix)
    n = len(matrix[0])
    visited = [[False for j in range(n)] for i in range(m)]

    import Queue
    queue = Queue.Queue()
    
    visited[r][c] = True
    queue.put((r,c))
    
    ans = False
    
    direction = [(1,0), (0,1), (-1,0), (0,-1)]

    while not queue.empty():
        x, y = queue.get()

        if x in (0, m-1) or y in (0, n-1):
            ans = True
            break

        for dx, dy in direction:
            new_x = x + dx
            new_y = y + dy
            if new_x >=0 and new_x < m and new_y >=0 and new_y < n and not visited[new_x][new_y] and matrix[x][y] > matrix[new_x][new_y]:
                queue.put((new_x, new_y))
    if ans:
        return "YES"
    else:
        return "NO"

mat = [
    [10,18,13],
    [9,8,7],
    [1,2,3]
]
r = 1
c = 1
print waterInjection(mat, r, c)
