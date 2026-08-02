class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a = set(list1) & set(list2)
        c = dict()
        for i in a:
            b = list1.index(i) + list2.index(i)
            c[i] = b
        min_value = min(c.values())
        return [k for k,v in c.items() if v == min_value]
        
        