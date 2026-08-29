class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Method - 1
        # dummy = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         dummy[j][i] = matrix[i][j]
        # return dummy

        # Method - 2
        return [list(row) for row in zip(*matrix)]