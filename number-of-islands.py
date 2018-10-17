import Queue
class Solution:
    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        queue = Queue.Queue()
        queue.put((i, j))
        grid[i][j] = 0 

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
         
        while not queue.empty():
            x, y = queue.get()
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[0]) or grid[new_x][new_y] == 0:
                    continue
                queue.put((new_x, new_y))
                grid[new_x][new_y] = 0

grid = [
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]

obj = Solution()
print obj.numIslands(grid)
