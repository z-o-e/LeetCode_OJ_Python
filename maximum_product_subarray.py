class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A)==1:
            return A[0]
        
        maxPre = minPre = A[0]
        res = A[0]
        
        for i in range(1, len(A)):
            maxCur = max(maxPre*A[i], minPre*A[i], A[i])
            minCur = min(maxPre*A[i], minPre*A[i], A[i])
            # keep track of optimal solution
            res = max(res, maxCur)
            # keep track of min & max track
            maxPre = maxCur
            minPre = minCur
            
        return res
