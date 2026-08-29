class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Method 1 
        # max_can = max(candies)
        # res = []
        # for i in candies:
        #     if i + extraCandies >= max_can:
        #         res.append(True)
        #     else:
        #         res.append(False)
        # return res



        # # Method 2
        # max_can = max(candies)
        # res = []

        # for i in candies:
        #     res.append(i + extraCandies >= max_can)
        # return res


        # Method - 3
        max_can = max(candies)
        return [i + extraCandies >= max_can for i in candies]