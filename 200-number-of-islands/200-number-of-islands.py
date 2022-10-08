class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i,j):
            if 0 <= i < rows and 0<= j < cols and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
            return
            
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count