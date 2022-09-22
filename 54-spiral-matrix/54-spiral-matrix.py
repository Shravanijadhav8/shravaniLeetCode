class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        def helper(i, j, currDir):
            nonlocal result
            if i < 0:
                i = 0
                return directions[currDir], i, j
            elif i > ROWS:
                i = ROWS
                
                return directions[currDir], i, j
            elif j < 0:
                j = 0
                return directions[currDir], i, j
            elif j > COLS:
                j = COLS
                return directions[currDir], i, j
            elif (i,j) in visited:
                if currDir == "A":
                    j -= 1
                elif currDir == "B":
                    i -= 1
                elif currDir == "C":
                    j += 1
                elif currDir == "D":
                    i += 1
                return directions[currDir], i, j
            else:
                visited.add((i,j))
                result.append(matrix[i][j])
                return currDir, i, j
            
            
        
        ROWS = len(matrix) - 1
        COLS = len(matrix[0]) - 1
        directions = {"A":"B", "B":"C", "C":"D", "D":"A"}
        currDir = "A"
        i, j = 0, 0
        visited = set()
        result = []
        
        while len(visited) < (ROWS+1)*(COLS+1):
            currDir, i, j = helper(i,j,currDir)
            if currDir == "A":
                j += 1
            if currDir == "B":
                i += 1
            if currDir == "C":
                j -= 1
            if currDir == "D":
                i -= 1
                
        return result
        
        