class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        l = 0
        min_len = float('inf')

        for r in range(n):
            summ += nums[r]

            while summ >= target:
                min_len = min(min_len, r - l + 1)
                summ -= nums[l]
                l += 1

        return min_len if min_len != float('inf') else 0