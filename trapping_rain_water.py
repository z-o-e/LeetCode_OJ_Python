class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        lenA = len(A)
        maxL, maxR = [0]*lenA, [0]*lenA
        
        for i in range(1,lenA):
            maxL[i] = max(maxL[i-1], A[i-1])
        
        for i in range(lenA-2,-1,-1):
            maxR[i] = max(maxR[i+1], A[i+1])
            
        res = 0
        for i in range(lenA):
            h = min(maxL[i],maxR[i])
            if h-A[i]>0:
                res += h-A[i]
                
        return res
