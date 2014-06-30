class Solution:
    # @return an integer
    def reverse(self, x):
        flag = 1
        if x<0:
            flag *= -1
            x *= -1
        
        res = 0
        
        while x!=0:
            res = res*10 + x%10
            x //= 10
            
        return res*flag
        