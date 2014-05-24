class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0:
            return 0
        
        occur = 1
        idx = 0
        
        for i in range(1,len(A)):
            if A[idx] != A[i]:
                idx += 1
                A[idx] = A[i]
                occur = 1
            else:
                if occur<2:
                    idx += 1
                    A[idx] = A[i]
                    occur+=1
        
        return idx+1