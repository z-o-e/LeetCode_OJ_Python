class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        a = {}
        for item in strs:
            tmp = ''.join(sorted(item))
            if a.has_key(tmp):
                a[tmp].append(item)
            else:
                a[tmp] = [item]
        
        res = []
        for key in a:
            if len(a[key])>1:
                res+=a[key]
                
        return res