from typing import List
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:


        n = len(s)

        # First and last occurrence of every character
        first = [n] * 26
        last = [-1] * 26

        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Try to construct the smallest valid interval
        # starting at first[c]
        for c in range(26):
            if last[c] == -1:
                continue

            left = first[c]
            right = last[c]

            i = left
            valid = True

            while i <= right:
                x = ord(s[i]) - ord('a')

                # This character appeared before `left`,
                # so we cannot include all its occurrences.
                if first[x] < left:
                    valid = False
                    break

                # We must include all occurrences of s[i].
                right = max(right, last[x])
                i += 1

            if valid:
                intervals.append((left, right))

        # Select intervals by earliest ending position.
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans