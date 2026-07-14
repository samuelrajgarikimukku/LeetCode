class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = sum(list(range(len(nums)+1)))
        b = sum(nums)
        return n-b


        ## Set Verions
        # s = set(range(len(nums)+1))
        # b = set(nums)
        # return next(iter(s-b))