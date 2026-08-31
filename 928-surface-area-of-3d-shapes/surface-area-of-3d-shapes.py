class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        #  Method - 1 
        # seen = set()
        # r = len(grid)
        # c = len(grid[0])
        # total = 0
        # remove = 0
        # for i in range(r):
        #     for j in range(c):
        #         if grid[i][j] == 0:
        #             h = 0
        #         else:
        #             h = (grid[i][j] - 1) * 2
        #         v = 0
        #         if i - 1 >= 0 and (i-1,j) not in seen:
        #             min_v = min(grid[i][j], grid[i-1][j])
        #             v += min_v*2
        #         if i + 1 < r and (i+1,j) not in seen:
        #             min_v = min(grid[i][j], grid[i+1][j])
        #             v += min_v*2
        #         if j - 1 >= 0 and (i,j-1) not in seen:
        #             min_v = min(grid[i][j], grid[i][j-1])
        #             v += min_v*2
        #         if j + 1 < c and (i,j+1) not in seen:
        #             min_v = min(grid[i][j], grid[i][j+1])
        #             v += min_v*2
        #         seen.add((i,j))
        #         total += grid[i][j]*6
        #         remove += h + v
        # return total - remove


        # Method - 2
        r = len(grid)
        c = len(grid[0])
        total = 0 
        for i in range(r):
            for j in range(c):
                h = grid[i][j]

                total += h*6
                total -= (h-1) * 2 if h > 0 else 0

                if i + 1 < r:
                    total -= min(h, grid[i+1][j]) * 2

                if j + 1 < c:
                    total -= min(h, grid[i][j+1])*2
        return total