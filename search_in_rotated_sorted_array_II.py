class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        
        lo = 0
        hi = len(A)-1
        
        while lo<=hi:
            mid = (lo+hi)//2
            
            if A[mid]==target:
                return True
            
            # lower-half sorted    
            if A[lo] < A[mid]:
                if target>=A[lo] and target<A[mid]:
                    hi = mid - 1
                else: 
                    lo = mid + 1
            # upper-half sorted       
            elif A[lo] > A[mid]:
                if target>A[mid] and target<=A[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            # escape duplicate
            else:
                lo+=1
        return False
        