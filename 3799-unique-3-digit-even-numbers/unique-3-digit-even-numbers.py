class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    if i == j or j == k or i == k:
                        continue

                    if digits[i] == 0:
                        continue

                    p = digits[i] * 100 + digits[j] * 10 + digits[k]

                    if p % 2 == 0:
                        nums.add(p)

        return len(nums)