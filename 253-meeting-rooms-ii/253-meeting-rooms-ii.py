import itertools
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startTimings = sorted(i[0] for i in intervals)
        endTimings = sorted(i[1] for i in intervals)
        
        startPointer, endPointer, usedRooms = 0, 0, 0
        
        while startPointer < len(intervals):
            if startTimings[startPointer] >= endTimings[endPointer]:
                usedRooms -= 1
                endPointer += 1
            usedRooms += 1
            startPointer += 1
        return usedRooms
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         intervals.sort(key = lambda x:x[0])
#         #intervals = list(i for i, _ in itertools.groupby(intervals))
#         print(f"intervlas:{intervals}")
        
        
        
#         if intervals == [] or len(intervals) == 1:
#             return 1
        
#         lowerBound, upperBound = intervals.pop(0)
#         i = 0
#         count = 1
        
        
        
#         while i < len(intervals):
#             left, right = intervals[i][0], intervals[i][1]
            
#             #if right == upperBound or left == lowerBound:
#                 #return count +1 
#             if left < upperBound and right > lowerBound:
#                 count += 1
#                 intervals.insert(i, [lowerBound, upperBound])
#                 i += 1
#                 lowerBound, upperBound = intervals[i][0], intervals[i][1]
#                 i += 1
#             else:
#                 intervals.insert(i, [lowerBound, upperBound])
#                 i += 1
#                 lowerBound, upperBound = intervals[i][0], intervals[i][1]
#                 del intervals[i]
#         return count
    #in this case there will be an interval which ends at 9 and there will be another interval which starts at 9 at any position