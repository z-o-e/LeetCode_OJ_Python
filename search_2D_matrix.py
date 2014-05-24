class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False
            
        low, high = 0, len(matrix)-1
        
        while low <= high:
            mid = (low+high)/2
            
            if target in (matrix[mid][0], matrix[mid][-1]):
                return True
            
            elif target > matrix[mid][-1]:
                low = mid + 1 
            
            elif target < matrix[mid][0]:
                high = mid - 1
                
            else:
                sublow, subhigh = 0, len(matrix[mid])-1
                
                while sublow <= subhigh:
                    submid = (sublow + subhigh) / 2
                    
                    if target==matrix[mid][submid]:
                        return True
                        
                    elif target>matrix[mid][submid]:
                        sublow = submid + 1
                    
                    else:
                        subhigh = submid - 1
                        
                return matrix[mid][submid]==target
        
        return False
    