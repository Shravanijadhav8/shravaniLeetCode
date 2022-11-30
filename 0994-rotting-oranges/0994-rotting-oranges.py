class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh, time = 0, 0
        visit = set()
        ROWS, COLS = len(grid) ,len(grid[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                    visit.add((i,j))
                if grid[i][j] == 2:
                    q.append([i,j])
        
        
        while q and visit:
            for _ in range(len(q)):
                i, j = q.popleft()
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in visit:  # check if adjacent orange is fresh
                        visit.remove(coord)
                        q.append(coord)
            time += 1
		# check if fresh oranges remain and return accordingly
        return -1 if visit else time
                    
                