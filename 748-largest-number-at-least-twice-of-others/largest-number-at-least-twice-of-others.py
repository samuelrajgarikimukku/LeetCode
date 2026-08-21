class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        k = nums.index(max(nums))
        nums.sort()
        if nums[-1] >= nums[-2] *2:
            return k
        return -1