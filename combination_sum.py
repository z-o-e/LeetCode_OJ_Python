class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
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
                tmp = cur[:]
                tmp.append(c)
                self.dfs(candidates, tmp, target-c)
