class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1 
        a = 0
        for i in range(len(digits)):
            a += digits[i] * (10**n)
            n -=1
        a += 1
        result = [int(d) for d in str(a)]
        return result

