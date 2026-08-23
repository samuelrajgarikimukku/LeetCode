class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Method - 1
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i + 1 < len(matrix) and j + 1 < len(matrix[0]):
        #             if matrix[i][j] != matrix[i+1][j+1]:
        #                 return False
        # return True


        # Method - 2
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row-1):
            for j in range(col-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False
        return True