class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2 :
            return False
        
        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for  i in range(n1):
            s1_arr[ord(s1[i]) - 97] += 1 
            s2_arr[ord(s2[i]) - 97] += 1 

        if s1_arr == s2_arr:
            return True

        for i in range(n1,n2):
            s2_arr[ord(s2[i]) - 97] += 1 
            s2_arr[ord(s2[i -n1]) - 97] -= 1 

            if s1_arr == s2_arr :
                return True
        return False

