class Solution:
    # @return a string
    def longestPalindrome(self, s):
        lenS = len(s)
        
        table = [[0 for i in range(lenS)] for i in range(lenS)]
        
        for i in range(lenS):
            table[i][i]=True
            head = i
            maxLen=1
            
        for i in range(lenS-1):
            if s[i]==s[i+1]:
                table[i][i+1] = True
                head = i
                maxLen=2
        
        for l in range(3,lenS+1,1):
            for i in range(lenS-l+1):
                j = i+l-1
                if s[i]==s[j] and table[i+1][j-1]:
                    table[i][j]=True
                    head = i
                    maxLen = l
                        
        return s[head:maxLen+i+1]