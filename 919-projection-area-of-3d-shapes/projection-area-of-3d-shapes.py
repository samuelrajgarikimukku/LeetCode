class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area = 0
        # Top
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    area += 1
        
        # Right
        for i in range(len(grid)):
            area += max(grid[i])
        
        # left 
        for j in range(len(grid[0])):
            max_col = 0
            for i in range(len(grid)):
                max_col = max(max_col, grid[i][j])
            area += max_col
        
        return area