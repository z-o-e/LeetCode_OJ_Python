class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        res = 0
        
        if num==[]:
            return res
        
        # hashmap: not visited then bag[item]=False, True otherwise
        bag = {}
        for item in num:
            bag[item] = False
            
        for item in bag:
            if bag[item]:
                continue
            
            count = 1
            
            elem = item + 1
            while elem in bag:
                bag[elem] = True
                count += 1
                elem += 1
            
            elem = item - 1
            while elem in bag:
                bag[elem] = True
                count += 1
                elem -= 1
                
            res = max(res, count)
        
        return res