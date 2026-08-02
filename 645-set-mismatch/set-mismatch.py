class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {i: 0 for i in range(1, len(nums) + 1)}

        for num in nums:
            count[num] += 1

        for num, freq in count.items():
            if freq == 2:
                duplicate = num
            elif freq == 0:
                missing = num

        return [duplicate, missing]
        
        