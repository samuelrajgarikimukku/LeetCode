class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        coll = {i:0 for i in range(1,len(nums)+1)}
        for i in nums:
            coll[i] += 1
        dup = max(coll,key=coll.get)
        real = min(coll,key=coll.get)
        return [dup,real]
        
        