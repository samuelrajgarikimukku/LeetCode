class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        seen = set()
        r = len(grid)
        c = len(grid[0])
        remove = 0
        total = 0
        for i in range(r):
            for j in range(c):
                seen.add((i,j))
                if grid[i][j] == 0:
                    height = 0
                else:
                    height = (grid[i][j] - 1) * 2
                v = 0
                if i-1 >= 0 and (i-1,j) not in seen:
                    min_v = min(grid[i][j], grid[i-1][j])
                    v += min_v*2
                if i + 1 < r and (i+1,j) not in seen:
                    min_v = min(grid[i][j], grid[i+1][j])
                    v += min_v*2
                if j-1 >= 0 and (i,j-1) not in seen:
                    min_v = min(grid[i][j], grid[i][j-1])
                    v += min_v*2
                if j+1 < c and (i,j+1) not in seen:
                    min_v = min(grid[i][j], grid[i][j+1])
                    v += min_v*2
                remove += height + v
                total += grid[i][j] * 6
        return total - remove