class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # min_val = min(nums)
        # max_val = max(nums)
        # b = [i for i in range(min_val,max_val+1)]
        # if b == nums:
        #     return []
        # c = list(set(b) - set(nums))
        # c.sort()
        # return c
        nums.sort()
        b = []
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                b.append(i)
        return b