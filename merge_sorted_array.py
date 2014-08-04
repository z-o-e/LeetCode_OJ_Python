class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        idxA = m-1
        idxB = n-1
        idx = m+n-1
        # note A already initialized
        while idxA>=0 and idxB>=0:
            if A[idxA]>=B[idxB]:
                A[idx] = A[idxA]
                idx -= 1
                idxA -= 1
            else:
                A[idx] = B[idxB]
                idx -= 1
                idxB -= 1
            
        while idxB>=0:
            A[idx] = B[idxB]
            idx -= 1
            idxB -= 1
            
        return A
                