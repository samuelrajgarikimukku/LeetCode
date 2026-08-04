# from collections import Counter
# class Solution:
#     def findShortestSubArray(self, nums: List[int]) -> int:
#         count = Counter(nums)
#         degree = max(count.values())
#         min_val = []
#         value = [k for k, v in count.items() if v == degree]
#         for i in value:
#             first_appearnce = nums.index(i)
#             last_idx = len(nums) - 1 - nums[::-1].index(i)
#             total = last_idx - first_appearnce + 1
#             min_val.append(total)
#         return min(min_val)




class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first = {}
        last = {}
        count = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        ans = len(nums)

        for num in count:
            if count[num] == degree:
                ans = min(ans, last[num] - first[num] + 1)

        return ans