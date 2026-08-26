class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        l = len(points)
        max_area = 0
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    area = abs(
                        points[i][0] * (points[j][1] - points[k][1])
                        + points[j][0] * (points[k][1] - points[i][1])
                        + points[k][0] * (points[i][1] - points[j][1])
                    ) / 2
                    max_area = max(max_area, area)
        return max_area