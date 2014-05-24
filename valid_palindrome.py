class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if not s:
            return True
        
        for c in s:
            if not('0'<=c<='9') and not('a'<=c<='z') and not('A'<=c<='Z') :
                s = s.replace(c,"")
        s = s.lower()     
        
        for i in range(len(s)/2):
            if s[i]!=s[len(s)-i-1]:
                return False
                
        return True