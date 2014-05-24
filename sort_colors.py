class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if not A:
            return A
        
        idx, red, blue =0, 0, len(A)-1

        while idx <= blue:
            if A[idx]==0:
                A[idx], A[red] = A[red], A[idx]
                red += 1
                idx += 1
            
            elif A[idx]==1:
                idx += 1
            
            else:
                # don't move idx when blue
                A[idx], A[blue] = A[blue], A[idx]
                blue -= 1
        
        return A