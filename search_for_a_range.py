class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        res = [-1, -1]
        
        if not A:
            return res
        
        idx = self.binarySearch(A, target)
        if idx==-1:
            return res
        
        left = right = idx
        while left>=0 and A[left]==target:
            left -= 1
        while right < len(A) and A[right]==target:
            right += 1
        
        return [left+1, right-1]
         
    def binarySearch(self, A, target):    
        low, high = 0, len(A)-1
        
        while low<=high:
            mid = (low+high)/2
            if target == A[mid]:
                return mid
            elif target < A[mid]:
                high = mid - 1
            else:
                low = mid + 1
                
        return -1
        