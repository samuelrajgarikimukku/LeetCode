class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return sum(num for num in freq if freq[num]  == 1)