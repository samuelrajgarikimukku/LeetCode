from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        
        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            """
            Number of distinct amounts <= x
            that are divisible by at least one coin.
            """
            n = len(coins)
            ans = 0

            # Inclusion-exclusion
            for mask in range(1, 1 << n):
                L = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        bits += 1
                        L = lcm(L, coins[i])

                        # This subset contributes 0
                        if L > x:
                            break
                else:
                    # Odd number of coins -> add
                    # Even number of coins -> subtract
                    if bits % 2:
                        ans += x // L
                    else:
                        ans -= x // L

            return ans

        # The kth amount cannot exceed
        # min(coins) * k
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left