class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval[0], newInterval[1]
        flag = False
        i = 0
        while i < len(intervals) and not flag:
            left, right = intervals[i][0], intervals[i][1]
            
            if ((start >= left and start <= right) and (end <= right and end >= left)) or (start <= left and end >= left) or (start <= right and start >= left and end >= right):
                start = min(start, left)
                end = max(end, right)
                del intervals[i]
                
            elif end < intervals[i][0]:
                intervals.insert(i, [start, end])
                flag = True
                break
            else: i+= 1
                
        if not flag:
            intervals.append([start, end])
        return intervals