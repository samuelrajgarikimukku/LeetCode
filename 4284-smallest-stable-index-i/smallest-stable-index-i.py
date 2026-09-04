class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # Method - 1 
        # n = len(nums)

        # for i in range(n):
        #     # Find maximum from index 0 to i
        #     max_val = nums[0]
        #     for j in range(0, i + 1):
        #         max_val = max(max_val, nums[j])

        #     # Find minimum from index i to n - 1
        #     min_val = nums[i]
        #     for j in range(i, n):
        #         min_val = min(min_val, nums[j])

        #     # Calculate instability score
        #     if max_val - min_val <= k:
        #         return i

        # return -1

        n = len(nums)

        # suffix_min[i] = minimum from i to n-1
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Keep track of maximum from 0 to i
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1