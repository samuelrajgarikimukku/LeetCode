class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]%2 != 0:
                    if nums[j]%2 == 0:
                        nums[i], nums[j] = nums[j], nums[i]
        return nums