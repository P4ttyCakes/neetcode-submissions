class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:


        new_start, new_end = newInterval
        res = []

        for i, (start,end) in enumerate(intervals):

            if end < new_start:
                res.append([start,end])

            
            elif start > new_end:
                res.append([new_start, new_end])
                res.extend(intervals[i:])
                return res
            

            #the intervals overlap, so we must make a new interval

            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)
        
        res.append([new_start, new_end])
        return res

            

            

            
            
            
            





        