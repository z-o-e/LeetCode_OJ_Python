class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        res = 0
        if not A or len(A)==1:
            return res
        
        # prev, curr tracks the previous and current maximum possible steps
        prev = curr = 0

        for i in range(len(A)):
            if (i>prev):
                prev = curr
                res += 1
            curr = max(curr, i+A[i])
            
        return res