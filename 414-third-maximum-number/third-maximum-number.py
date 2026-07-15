class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        b = list(set(nums))
        b.sort()
        if len(b) < 3:
            return max(b)
        i = 0
        while i < 2:
            b.pop()
            i += 1
        return b[-1]
        
    
