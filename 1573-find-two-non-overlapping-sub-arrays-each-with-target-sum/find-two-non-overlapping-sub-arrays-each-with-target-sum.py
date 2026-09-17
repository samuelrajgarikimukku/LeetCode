class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # best[i] = minimum length of a valid subarray
        # completely inside arr[0:i]
        best = [float('inf')] * (n + 1)

        left = 0
        curr_sum = 0
        ans = float('inf')

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum is too large
            while left <= right and curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Found a subarray [left, right] with sum == target
            if curr_sum == target:
                length = right - left + 1

                # Combine it with the best subarray ending before `left`
                if best[left] != float('inf'):
                    ans = min(ans, length + best[left])

                # Update best for prefixes up to right
                best[right + 1] = min(best[right], length)

            else:
                best[right + 1] = best[right]

        return -1 if ans == float('inf') else ans