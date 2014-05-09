class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if not needle:
            return haystack    
        
        if len(needle)>len(haystack):
            return None
        
        if needle==haystack:
            return haystack
        
        for i in range(len(haystack)-len(needle)):
            if needle==haystack[i:i+len(needle)]:
                return haystack[i:]
                
        return None