class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row,col = len(img), len(img[0])


        for r in range(row):
            for c in range(col):
                total,cnt = 0,0
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if i < 0 or i == row or j < 0 or j == col:
                            continue
                        total += img[i][j] % 256
                        cnt += 1
                img[r][c] = img[r][c] ^ (total // cnt) << 8
        for r in range(row):
            for c in range(col):
                img[r][c] = img[r][c] >> 8
        return img
        