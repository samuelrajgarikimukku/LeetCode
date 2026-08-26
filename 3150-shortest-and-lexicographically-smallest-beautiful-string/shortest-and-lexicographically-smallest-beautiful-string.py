class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # We have at least k ones
            while ones >= k:
                # Exactly k ones -> candidate
                if ones == k:
                    candidate = s[left:right + 1]

                    if (best == "" or
                        len(candidate) < len(best) or
                        (len(candidate) == len(best) and candidate < best)):
                        best = candidate

                # Move left pointer
                if s[left] == '1':
                    ones -= 1
                left += 1

        return best