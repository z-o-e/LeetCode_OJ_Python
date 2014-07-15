class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        return self.findCombinations([i for i in range(1, n+1)], k)
        
    def findCombinations(self, nums, k):
        sol  = []
        
        if k==0:
            return sol
            
        for i in range(len(nums)):
            if k==1:
                sol.append([nums[i]])
                
            else:
                for n in self.findCombinations(nums[i+1:], k-1):
                    sol.append([nums[i]] + n)
                    
        return sol
        