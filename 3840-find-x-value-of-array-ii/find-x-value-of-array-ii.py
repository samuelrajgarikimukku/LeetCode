class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:

        seg = SegmentTree(nums, k)

        ans = []

        for index, value, start, x in queries:

            # Persistent update
            seg.point_update(index, value)

            # We need all non-empty prefixes of nums[start:]
            _, prefix_count = seg.range_query(start, len(nums) - 1)

            ans.append(prefix_count[x])

        return ans


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k
        self.tree = [(1, [0] * k) for _ in range(4 * self.n)]

        self.nums = nums
        self.build(1, 0, self.n - 1)

    def merge(self, left, right):
        left_prod, left_pref = left
        right_prod, right_pref = right

        # Product of the whole combined segment
        prod = (left_prod * right_prod) % self.k

        # Prefixes of the combined segment
        pref = [0] * self.k

        # Prefixes completely inside the left segment
        for r in range(self.k):
            pref[r] += left_pref[r]

        # Prefixes that go through the left segment
        # and then take a prefix of the right segment.
        for r in range(self.k):
            new_rem = (left_prod * r) % self.k
            pref[new_rem] += right_pref[r]

        return prod, pref

    def build(self, node, l, r):
        if l == r:
            rem = self.nums[l] % self.k

            pref = [0] * self.k
            pref[rem] = 1

            self.tree[node] = (rem, pref)
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update(self, node, l, r, idx, value):
        if l == r:
            rem = value % self.k

            pref = [0] * self.k
            pref[rem] = 1

            self.tree[node] = (rem, pref)
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, value)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, value)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node, l, r, ql, qr):
        # Completely outside
        if qr < l or r < ql:
            # Identity segment:
            # product = 1, no non-empty prefixes
            return 1, [0] * self.k

        # Completely inside
        if ql <= l and r <= qr:
            return self.tree[node]

        mid = (l + r) // 2

        left = self.query(node * 2, l, mid, ql, qr)
        right = self.query(node * 2 + 1, mid + 1, r, ql, qr)

        return self.merge(left, right)

    def point_update(self, idx, value):
        self.update(1, 0, self.n - 1, idx, value)

    def range_query(self, left, right):
        return self.query(1, 0, self.n - 1, left, right)