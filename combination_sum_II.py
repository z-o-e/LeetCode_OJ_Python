class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        self.res = []
        self.dfs(candidates, self.res, [], target)
        
        return self.res
        
    def dfs(self, candidates, res, cur, target):
        if target==0 and cur:
            cur = sorted(cur)
            if cur not in res:
                res.append(cur)
            return
            
        if not candidates:
            return 
        
        for i in range(len(candidates)):
            if candidates[i]<=target:
                tmp = cur[:]
                tmp.append(candidates[i])
                self.dfs(candidates[i+1:], res, tmp, target-candidates[i])
        
