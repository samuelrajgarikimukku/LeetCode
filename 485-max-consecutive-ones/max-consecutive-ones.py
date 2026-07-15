class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        dist = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] != 1:
                l = r+1
            if nums[r] == 1:
                dist = max(dist, r-l+1)
            r += 1
                
        return dist