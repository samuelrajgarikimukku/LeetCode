class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums:
            return res
        l = nums[0]
        i = l + 1
        r = 1
        while r < len(nums):
            if nums[r] != i:
                if nums[r - 1] == l:
                    res.append(str(l))
                else:
                    res.append(str(l) + "->" + str(nums[r - 1]))
                l = nums[r]
                i = l + 1
                r += 1
            else:
                i += 1
                r += 1
        # Append the last pending range
        if nums[-1] == l:
            res.append(str(l))
        else:
            res.append(str(l) + "->" + str(nums[-1]))
        return res