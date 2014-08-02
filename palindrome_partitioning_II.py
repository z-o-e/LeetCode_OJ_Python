class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        sLen = len(s)
        
        isPalindrome = [ [True for i in range(sLen)] for i in range(sLen)]
        for l in range(2,sLen+1):
            for i in range(sLen-l+1):
                j = i+l-1
                if l==2:
                    isPalindrome[i][j] = (s[i]==s[j])
                else:
                    isPalindrome[i][j] = (s[i]==s[j] and isPalindrome[i+1][j-1])
            
        dp = [0]*sLen
        for i in range(sLen-1, -1, -1):
            if isPalindrome[i][sLen-1]:
                continue
            else:
                cut = 1000000
                for j in range(i+1,sLen):
                    if isPalindrome[i][j-1]:
                        cut = min(dp[j]+1,cut)
                        
                dp[i] = cut
                
        return dp[0]