class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(list(range(len(nums)+1)) + nums)
        n = set(nums)
        k = s - n
        k = next(iter(k))
        return int(k)
        