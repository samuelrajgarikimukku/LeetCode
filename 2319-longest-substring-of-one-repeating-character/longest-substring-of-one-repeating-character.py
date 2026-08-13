class SegmentTree:
    def __init__(self, s):
        self.n = len(s)
        self.tree = [None] * (4 * self.n)
        self.s = list(s)
        self.build(1, 0, self.n - 1)

    def make_node(self, ch, length=1):
        return {
            "length": length,
            "left": ch,
            "right": ch,
            "prefix": length,
            "suffix": length,
            "best": length
        }

    def merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        res = {
            "length": a["length"] + b["length"],
            "left": a["left"],
            "right": b["right"],
            "prefix": a["prefix"],
            "suffix": b["suffix"],
            "best": max(a["best"], b["best"])
        }

        # If the boundary characters are equal,
        # the suffix of a and prefix of b can be combined.
        if a["right"] == b["left"]:
            combined = a["suffix"] + b["prefix"]

            res["best"] = max(res["best"], combined)

            # Entire left part is one repeating character
            if a["prefix"] == a["length"]:
                res["prefix"] = a["length"] + b["prefix"]

            # Entire right part is one repeating character
            if b["suffix"] == b["length"]:
                res["suffix"] = a["suffix"] + b["length"]

        return res

    def build(self, node, l, r):
        if l == r:
            self.tree[node] = self.make_node(self.s[l])
            return

        mid = (l + r) // 2

        self.build(node * 2, l, mid)
        self.build(node * 2 + 1, mid + 1, r)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update(self, node, l, r, idx, ch):
        if l == r:
            self.s[idx] = ch
            self.tree[node] = self.make_node(ch)
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(node * 2, l, mid, idx, ch)
        else:
            self.update(node * 2 + 1, mid + 1, r, idx, ch)

        self.tree[node] = self.merge(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def update_index(self, idx, ch):
        self.update(1, 0, self.n - 1, idx, ch)

    def get_best(self):
        return self.tree[1]["best"]


class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        seg = SegmentTree(s)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            seg.update_index(idx, ch)
            ans.append(seg.get_best())

        return ans