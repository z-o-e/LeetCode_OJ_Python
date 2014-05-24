class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        words = s.split()
        res = ""
        
        while words:
            if len(words)==1:
                res += words.pop()
            else:            
                res += words.pop()+" "
                
        return res