class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        result = nums[:]

        start = 0

        while start < n:
            end = start

            # Find a connected group.
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Indices in the original array
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            # Values are already sorted
            values = [arr[i][0] for i in range(start, end + 1)]

            # Put smallest values at smallest indices
            for i, value in zip(indices, values):
                result[i] = value

            start = end + 1

        return result