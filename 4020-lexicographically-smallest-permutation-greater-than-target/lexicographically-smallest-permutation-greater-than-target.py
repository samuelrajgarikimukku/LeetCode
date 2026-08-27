class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        ans = []

        for i in range(len(target)):
            t = ord(target[i]) - ord('a')

            # Try to keep the prefix equal to target.
            if cnt[t] > 0:
                cnt[t] -= 1
                ans.append(target[i])
                continue

            # Cannot match target[i].
            # Find the smallest character greater than target[i].
            for c in range(t + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1
                    ans.append(chr(c + ord('a')))

                    # Fill remaining positions with smallest characters.
                    for x in range(26):
                        ans.extend(chr(x + ord('a')) * cnt[x])

                    return ''.join(ans)

            # No character >= target[i] is possible here.
            # We need to backtrack and change an earlier position.
            break

        # target itself was possible, but we need a STRICTLY greater permutation.
        # Backtrack to find the rightmost position that can be increased.
        for i in range(len(ans) - 1, -1, -1):
            c = ord(ans[i]) - ord('a')
            cnt[c] += 1

            t = ord(target[i]) - ord('a')

            # Find the smallest available character > target[i].
            for bigger in range(t + 1, 26):
                if cnt[bigger] > 0:
                    cnt[bigger] -= 1

                    result = ans[:i]
                    result.append(chr(bigger + ord('a')))

                    # Fill the suffix with smallest characters.
                    for x in range(26):
                        result.extend(chr(x + ord('a')) * cnt[x])

                    return ''.join(result)

        return ""