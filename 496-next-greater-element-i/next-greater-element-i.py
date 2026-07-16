class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        box = []

        for l in range(len(nums1)):
            for r in range(len(nums2)):
                if nums1[l] == nums2[r]:
                    for k in range(r + 1, len(nums2)):
                        if nums2[k] > nums1[l]:
                            box.append(nums2[k])
                            break
                    else:
                        box.append(-1)
                    break

        return box