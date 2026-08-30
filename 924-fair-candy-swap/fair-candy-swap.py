class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(bobSizes) - sum(aliceSizes)) // 2

        bob_set = set(bobSizes)

        for alice in aliceSizes:
            bob = alice + diff

            if bob in bob_set:
                return [alice, bob]