# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        if not newInterval:
            return intervals
        if not intervals:
            return [newInterval]
        
        res = []
        while intervals!=[]:
            if newInterval.start > intervals[0].end:
                res += [intervals[0]] + [newInterval]
                
            elif newInterval.end < intervals[0].start:
                res += [newInterval] + [intervals[0]]
                
            else:
                newInterval.start = min(intervals[0].start, newInterval.start)
                newInterval.end = max(intervals[0].end, newInterval.end)
                res += [newInterval] + intervals[1:]
                break
                
            intervals = intervals[1:]
            
        return res
            