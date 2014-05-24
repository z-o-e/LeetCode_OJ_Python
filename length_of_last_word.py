class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        t=s.split(' ')
        if len(t)==0:
            return 0
        
        while t.count('')!=0:
            t.remove('')
        
        if len(t)!=0: 
            return len(t[-1])
        
        return 0