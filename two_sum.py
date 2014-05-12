class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        d = {}
        
        for i in range(len(num)):
            if target - num[i] in d:
                return (d[target - num[i]]+1, i+1)
            else:
                d[num[i]] = i
                
        return (d[target - num[i]]+1, i+1)