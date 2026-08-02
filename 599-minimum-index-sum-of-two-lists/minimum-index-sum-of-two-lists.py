class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pos = {name: i for i, name in enumerate(list1)}

        ans = []
        min_sum = float('inf')

        for j, name in enumerate(list2):
            if name in pos:
                s = pos[name] + j
                if s < min_sum:
                    min_sum = s
                    ans = [name]
                elif s == min_sum:
                    ans.append(name)

        return ans