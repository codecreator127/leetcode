class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs

        queue = []

        distX = [-1, 1, 0, 0]
        distY = [0, 0, 1, -1]

        # do bfs from all rotten oranges

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        time = 0
        visited = set()

        while queue:
            row, col, t = queue.pop(0)

            for i in range(4):
                newRow = row + distX[i]
                newCol = col + distY[i]

                if newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]) and grid[newRow][newCol] == 1:
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol, t + 1))

            time = t
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return time
