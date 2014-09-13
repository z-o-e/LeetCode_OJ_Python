# dp ---O(n^2)time, O(n)space f(i) = any_of(f(j)&&s[j + 1, i] in dict), 0 <= j < i
# dfs --- tle O(2^n)time, O(n)space
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        sLen  = len(s)
        f = [False for i in range(sLen+1)]
        f[0] = True
        
        for i in range(1, sLen+1):
            for j in range(i):

                if f[j] and s[j:i] in dict:
                    f[i] = True
                          
        return f[-1]
    
