class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        for i in range(len(A)):
            while A[i]>0 and A[i]!=i+1 and A[i]<=len(A):
                if A[i]==A[A[i]-1]:
                    break
                A[A[i]-1], A[i] = A[i], A[A[i]-1]

        for i in range(len(A)):
            if A[i]<0 or A[i]!=i+1:
                return i+1
                
        return len(A)+1
                