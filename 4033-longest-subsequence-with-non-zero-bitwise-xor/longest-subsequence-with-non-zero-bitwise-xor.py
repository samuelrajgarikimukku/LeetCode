class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0

        for x in nums:
            xor ^= x

        # If total XOR is non-zero, take all elements.
        if xor != 0:
            return len(nums)

        # Total XOR is zero. Remove one non-zero element;
        # the remaining XOR becomes non-zero.
        for x in nums:
            if x != 0:
                return len(nums) - 1

        # All elements are zero.
        return 0