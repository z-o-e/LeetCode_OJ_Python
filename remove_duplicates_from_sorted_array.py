class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A)==0:
            return 0;
        idx = 0;
        for i in range(1,len(A)):
            if (A[i]!=A[idx]):
                idx+=1
                A[idx] = A[i] 
        return idx+1