class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        
        lo = 0
        hi = len(A)-1
        
        while (lo<=hi):
            mid = (lo+hi)//2
            
            if A[mid]==target:
                return mid
            
            # lower-half is strictly sorted
            if A[lo]<=A[mid]:
                # if target is within this range
                if target>=A[lo] and target<A[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
            # upper-half is strictly sorted
            else:
                if target>A[mid] and target<=A[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1