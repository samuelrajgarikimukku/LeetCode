class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        min_odd = float('inf')
        min_even = float('inf')

        for x in nums1:
            if x % 2:
                min_odd = min(min_odd, x)
            else:
                min_even = min(min_even, x)

        can_make_odd = True
        can_make_even = True

        for x in nums1:
            # Can x become odd?
            if x % 2 == 1:
                continue

            # Need a smaller odd number
            if min_odd >= x:
                can_make_odd = False
                break

        for x in nums1:
            # Can x become even?
            if x % 2 == 0:
                continue

            # Need a smaller odd number? No:
            # odd - odd = even, so need a smaller odd number.
            if min_odd >= x:
                can_make_even = False
                break

        return can_make_odd or can_make_even