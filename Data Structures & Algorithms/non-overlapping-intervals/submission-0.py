class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key= lambda x: x[1])
        removed = 0

        res = []


        for start, end in intervals: 

            if not res or start >= res[-1][1]:
                res.append([start, end])
            
            else:
                removed+=1
        
        return removed


        