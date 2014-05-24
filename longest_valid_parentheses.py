class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        # idx tracks the position of the last ')'
        idx, res = -1, 0
        
        if len(s) < 2:   
            return res
            
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                # current match sequence breaks, update idx
                if not stack:
                    idx = i
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i-idx)
                    else:
                        res = max(res, i-stack[-1])
        
        return res