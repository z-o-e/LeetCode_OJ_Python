# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        
        intervals.sort(key = lambda x: x.start)
        
        i = 1
        while i < len(intervals):
            
            if intervals[i].start <= intervals[i-1].end:
                # merge
                if intervals[i].end >= intervals[i-1].end:
                    intervals[i].start = intervals[i-1].start
                    del intervals[i-1]
                else:
                    del intervals[i]
                    
            else:
                i += 1
                
        return intervals