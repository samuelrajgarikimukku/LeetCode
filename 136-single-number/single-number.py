class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        from collections import Counter
        b = Counter(nums)
        for key,value in b.items():
            if value == 1 :
                return key
        