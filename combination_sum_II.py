class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates = sorted(candidates)
        self.res = []
        self.dfs(candidates, [], target)
        
        return self.res
        
    def dfs(self, candidates, cur, target):
        if target==0:
            if sorted(cur) not in self.res:
                self.res.append(cur)
            return 
        
        for c in candidates:
            if target-c>=0:
                tmp, ctmp = cur[:], candidates[:]
                tmp.append(c)
                ctmp.remove(c)
                self.dfs(ctmp, tmp, target-c)