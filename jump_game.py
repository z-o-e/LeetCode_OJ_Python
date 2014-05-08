class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        n = len(A)
        reach = 1
        
        for i in range(n):
            if i<reach and reach<n:
                # reach takes the maximum possible jump at every step
                reach = max(reach, i+1+A[i])
            
        return reach >= n
        