from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        degree = max(count.values())
        min_val = []
        value = [k for k, v in count.items() if v == degree]
        for i in value:
            first_appearnce = nums.index(i)
            last_idx = len(nums) - 1 - nums[::-1].index(i)
            total = last_idx - first_appearnce + 1
            min_val.append(total)
        return min(min_val)