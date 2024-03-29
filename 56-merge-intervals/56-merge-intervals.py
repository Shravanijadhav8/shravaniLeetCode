class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        lowerBound, upperBound = intervals.pop(0)
        i = 0
        
        while i < len(intervals):
            left, right = intervals[i][0], intervals[i][1]
            
            if (right >= lowerBound) and  (left <= upperBound):
                lowerBound = min(lowerBound, left)
                upperBound = max(upperBound, right)
                del intervals[i]
                
            else:
                intervals.insert(i, [lowerBound, upperBound])
                i += 1
                lowerBound, upperBound = intervals[i][0], intervals[i][1]
                del intervals[i]
    
                
        
        if [lowerBound, upperBound] not in intervals:
            intervals.append([lowerBound,upperBound])
        return intervals
                