class Solution:
    # @return an integer
    def romanToInt(self, s):
        R2I = {}
        R2I['I'], R2I['V'], R2I['X'] = 1, 5, 10
        R2I['L'], R2I['C'], R2I['D'], R2I['M'] = 50, 100, 500, 1000
        
        # scan from msd -> lsd, 
        # minus if smaller value symbol is before the large value symbol
        # plus otherwise
        # e.g. IV=5-1, VI=5+1, II=1+1 CIV=100+1
        res = 0
        for i in range(len(s)):
            if i>0 and R2I[s[i]]>R2I[s[i-1]]:
                res += R2I[s[i]]-2*R2I[s[i-1]]
            else:
                res += R2I[s[i]]
        return res