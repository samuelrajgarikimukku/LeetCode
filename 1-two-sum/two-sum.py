class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for l in range(n):
            for r in range(l + 1, n):
                if nums[l] + nums[r] == target:
                    return [l,r]
        return []
