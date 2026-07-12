from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    # Boyer-Moore Voting Algorithm
        # count = 0
        # candidate = None

        # for num in nums:
        #     if count == 0:
        #         candidate = num

        #     if num == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate
        b = Counter(nums)
        for key, value in b.items():
            if value > len(nums)/2:
                return(key)


        