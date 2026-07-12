class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        ## Brute Force
        # for i in range (len(nums)):
        #     for j in range(i+1, min(i+k+1,len(nums))):
        #         if nums[i] == nums[j]:
        #             return True
        # return False
        

        # Sliding Window technique
        window = set()
        L = 0 

        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False