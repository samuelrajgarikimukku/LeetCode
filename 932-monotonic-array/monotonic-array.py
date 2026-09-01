class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # # Method - 1
        # increase, decrease = True, True
        # for i in range(len(nums)-1):
        #     if not (nums[i] <= nums[i+1]):
        #         increase =  False
        #     if not (nums[i] >= nums[i+1]):
        #         decrease = False
        # return increase or decrease

        # Method - 2 
        if nums[-1] - nums[0] < 0:
            nums.reverse()
        for i in range(len(nums)-1):
            if not (nums[i] <= nums[i+1]):
                return False
        return True