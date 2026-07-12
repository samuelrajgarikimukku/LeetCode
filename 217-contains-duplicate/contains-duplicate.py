from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for key,values in count.items():
            if values >= 2:
                return True
                break
        else:
            return False
        