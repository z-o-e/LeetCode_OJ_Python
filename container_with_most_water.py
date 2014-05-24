class Solution:
    # @return an integer
    def maxArea(self, height):
        res = 0
        if not height:
            return 0
            
        start, end = 0, len(height)-1
        
        while start<end:
            res = max( res, (end-start) * min(height[start], height[end]) )
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return res 
                