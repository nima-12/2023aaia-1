class Solution:
    def isPowerOfTwo(self,n: int) -> bool:
        if n <= 0:
            return false
        
        while n>1:
            if n%2!=0:
                return False
            else:
                n = n // 2
    
        return True