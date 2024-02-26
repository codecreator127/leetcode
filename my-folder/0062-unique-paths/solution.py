class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        grid = [[0] * m for i in range(n)]
        grid[0][0] = 1

        for i in range(1, m):
            grid[0][i] = grid[0][i-1]

        for j in range(1, n):
            grid[j][0] = grid[j - 1][0]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        print(grid)

        return grid[n - 1][m - 1]
