class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        if len(height)==1:
            return height[0]
            
       
        stack, res = [], 0
        i=0
        while i<len(height):
             # maintain a stack of index of heights, heights are in increasing order
            if not stack or height[i]>=height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                prevIdx = stack.pop()
                if not stack:
                    # empty stack after the last element is popped
                    cur = height[prevIdx]*i
                else:
                    # calculate area till the point where last element is popped
                    cur = height[prevIdx]*(i-stack[-1]-1)

                res = max(res,cur)
    
        # similar to previous        
        while stack:
            prevIdx = stack.pop()
            if not stack:
                cur = height[prevIdx]*i
            else:
                cur = height[prevIdx]*(i-stack[-1]-1)

            res = max(res,cur)
                
        return res