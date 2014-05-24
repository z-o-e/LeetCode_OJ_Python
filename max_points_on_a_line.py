# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if not points:
            return 0
        
        res = 1 
    
        for i in range(len(points)-1):
            ax, ay = points[i].x, points[i].y
            slopes = {}
            
            for j in range(i+1, len(points)):
                bx, by = points[j].x, points[j].y
                
                if (ax,ay)==(bx,by):
                    if 'duplicates' not in slopes:
                        slopes['duplicates'] = 2
                    else:
                        slopes['duplicates'] += 1
                    
                elif ay==by:
                    if 'vertical' not in slopes:
                        slopes['vertical'] = 2
                    else:
                        slopes['vertical'] += 1
                        
                else:
                    # float!!
                    s = 1.*(ax-bx)/(ay-by)
                    if s not in slopes:
                        slopes[s] = 2
                    else:
                        slopes[s] += 1
            
            if 'duplicates' not in slopes or len(slopes)<2:
                ss = slopes[max(slopes, key = slopes.get)]
            else:
                if max(slopes, key = slopes.get) == 'duplicates':
                    ss = slopes[ sorted(slopes,key = slopes.get)[1] ] + slopes['duplicates'] - 1
                else:
                    ss = slopes[max(slopes, key = slopes.get)] + slopes['duplicates'] - 1
    
            res = max(ss,res)
            
            # if max points exceeds points left, exit early
            if res >= len(points) - i:
                break
    
        return res