class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            # Find maximum from index 0 to i
            max_val = nums[0]
            for j in range(0, i + 1):
                max_val = max(max_val, nums[j])

            # Find minimum from index i to n - 1
            min_val = nums[i]
            for j in range(i, n):
                min_val = min(min_val, nums[j])

            # Calculate instability score
            if max_val - min_val <= k:
                return i

        return -1