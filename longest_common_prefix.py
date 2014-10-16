class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ''
        if len(strs)==1:
            return strs[0]
        
        strs = sorted(strs, key = lambda x: len(x))
        if strs[0]=='':
            return ''
            
        prefix = 0
        while prefix < min(len(strs[0]), len(strs[1])) and strs[0][prefix]==strs[1][prefix]:
            prefix += 1
        prefix -= 1
        
        for i in range(1,len(strs)-1):
            c = min(len(strs[i+1]), prefix+1)
            for j in range(c):
                if strs[i+1][j]!=strs[i][j]:
                    prefix = j-1
                    break
                    
        return strs[0][:prefix+1]

