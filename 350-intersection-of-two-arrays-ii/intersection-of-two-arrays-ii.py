from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_list = Counter(nums1)
        res = []

        for num in nums2:
            if my_list[num] > 0:
                res.append(num)
                my_list[num] -= 1
        return res