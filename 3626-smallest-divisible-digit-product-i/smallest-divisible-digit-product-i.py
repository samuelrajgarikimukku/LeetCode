class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            # 1. Separate check: Convert to string to look for "0"
            if "0" in str(n):
                return n  # Fixed: returns 'n' instead of 'm'
            
            # 2. Calculate product if no "0" is found
            temp = n
            product = 1
            while temp > 0:
                product *= temp % 10
                temp //= 10  # Fixed: added assignment operator (=)
                
            # 3. Check divisibility
            if product % t == 0:
                return n 
            
            # 4. Increment to the next number
            n += 1
