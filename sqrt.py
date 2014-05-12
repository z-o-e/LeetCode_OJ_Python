class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x<=0:
            return x
        
        root = x
        guess = 0
        
        while abs(root-guess)>0.0001:
            guess = root
            root = 0.5*(root + x / root )
            
        return int(root)
        