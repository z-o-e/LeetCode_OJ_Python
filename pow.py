class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        # x^n = x^(n/2) * x^(n/2) * x^(n%2) when n>0
        # x^n = 1.0 / [ x^(-n/2) * x^(-n/2) * x^(-n%2) ] when n<0
        if n<0:
            return 1.0 / self.power(x, -n)
        else:
            return self.power(x,n)
        
    def power(self, x, n):
        # recursive but divide first!
        if n==0:
            return 1
        
        z = self.power(x, n/2)
        
        if n%2==0:
            return z*z
        return z*z*x
        