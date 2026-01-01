class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        distX = [-1, 1, 0, 0]
        distY = [0, 0, 1, -1]

        queue = [(entrance[0], entrance[1], 0)]
        visited = set()

        # do BFS  
        while queue:
            row, col, count = queue.pop(0)
            if (row, col) in visited:
                continue

            visited.add((row, col))

            if (row != entrance[0] or col != entrance[1]) and (row == 0 or col == 0 or row == len(maze) - 1 or col == len(maze[0]) - 1):
                return count
                
            # add all dirctions to queue
            for i in range(4):
                newRow = row + distX[i]
                newCol = col + distY[i]

                if 0 <= newRow < len(maze) and 0 <= newCol < len(maze[0]) and maze[newRow][newCol] == ".":
                    queue.append((newRow, newCol, count + 1))
                
        return -1
