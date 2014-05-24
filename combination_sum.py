class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        dp={}
        dp[0]=[[]]
        for i in range(1,target+1):
            dp[i]=[]
            for c in candidates:
                if c<=i and dp[i-c]:
                    for item in dp[i-c]:
                        tmp = sorted([c]+item)
                        if tmp not in dp[i]:
                            dp[i].append(tmp)
        
        return dp[target] 
        
