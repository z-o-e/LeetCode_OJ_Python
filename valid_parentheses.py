class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return False
        
        left = "{[("
        right = "}])"
        stack = []
        
        while s:
            if not stack:
                    stack.append(s[0])
            elif s[0] in left:
                stack.append(s[0])
            else:
                if stack[-1] in left:
                    if left.index(stack[-1])==right.index(s[0]):
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(s[0])
            s = s[1:]
        
        if not stack:
            return True
        return False
    