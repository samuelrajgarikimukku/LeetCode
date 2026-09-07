class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i, j = 0, len(nums) - 1

        while i < j:
            # Find an odd number from the left
            while i < j and nums[i] % 2 == 0:
                i += 1

            # Find an even number from the right
            while i < j and nums[j] % 2 != 0:
                j -= 1

            # Swap
            nums[i], nums[j] = nums[j], nums[i]

        return nums
