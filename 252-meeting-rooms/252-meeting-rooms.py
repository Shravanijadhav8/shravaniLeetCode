class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key= lambda x:x[0])
        
        if intervals == [] or len(intervals) == 1:
            return True
        
        lowerBound, upperBound = intervals.pop(0)
        i=0
        while i < len(intervals):
            left, right = intervals[i][0], intervals[i][1]
            if (right > lowerBound) and  (left < upperBound):
                return False
           
            else:
                #del intervals[i]
                #if [lowerBound, upperBound] not in intervals:
                intervals.insert(i, [lowerBound, upperBound])
                i += 1
                lowerBound, upperBound = intervals[i][0], intervals[i][1]
                i+=1
                #left, right = intervals[i][0], intervals[i][1]
        return True
        
        
            