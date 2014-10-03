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
        if not intervals:
            return [newInterval]
        
        # idea: insert newInterval, keeping intervals sorted by first element --> merge interval
        if newInterval.start <= intervals[0].start:
            # insert at head
            intervals =  [newInterval]+intervals
            startIdx = 1
        elif newInterval.start >= intervals[-1].start:
            # insert at tail
            intervals.append(newInterval)
            startIdx = len(intervals)-1
        else:
            # insert in the middle
            for i in range(len(intervals)):
                if newInterval.start < intervals[i].start:
                    intervals = intervals[:i] + [newInterval] + intervals[i:]
                    startIdx = i
                    break
                    
        return self.merge(intervals, startIdx)
   
    def merge(self, intervals, startIdx):
        # check and merge intervals starting from startIdx
        i = startIdx
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
        
                    
