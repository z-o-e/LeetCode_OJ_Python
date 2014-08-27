class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if digits=="":
            return [""]
            
        alphs = []
        for dig in digits:
            alphs.append(self.lookup(int(dig)))
            
        self.res = []
        self.combinations(0, alphs)
        return self.res
        
    def combinations(self, idx, arr):
        if idx > len(arr)-1:
            return
        
        tmp = []

        for a in arr[idx]:            
            if idx==0:
                tmp.append(a)                
            else:                
                for r in self.res:
                    tmp.append(r+a)
                                
        self.res = tmp
        
        return self.combinations(idx+1, arr)
        
    def lookup(self, numStr):
        d={}
        d[2], d[3], d[4], d[5] = 'abc', 'def', 'ghi', 'jkl'
        d[6], d[7], d[8], d[9] = 'mno', 'pqrs', 'tuv', 'wxyz'
        
        if numStr not in d:
            return 
        
        return d[numStr]