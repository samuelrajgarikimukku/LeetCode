class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Method - 1 
        # i = 1
        # while True:
        #     if k*i not in nums:
        #         return k*i
        #     i += 1

        # Method - 2
        num_set = set(nums)
        i = 1

        while k*i in num_set:
            i += 1
        return k*i