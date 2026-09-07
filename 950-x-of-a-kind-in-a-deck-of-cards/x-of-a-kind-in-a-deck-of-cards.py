from collections import Counter
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dec = Counter(deck)

        x = 0
        for value in dec.values():
            x = gcd(x, value)

        return x >= 2