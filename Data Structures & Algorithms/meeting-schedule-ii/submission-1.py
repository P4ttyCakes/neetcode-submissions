"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        ans = 0

        intervals.sort(key = lambda x: x.start)

        heap = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            if not heap:
                #pushing it in by start_time
                heapq.heappush(heap, [end, start])
            
            else:


                #check to see if the spot opened up, and push in meeting room
                old_end, old_start = heapq.heappop(heap)

                if old_end <= start:
                    heapq.heappush(heap, [end, start])

                else:
                    heapq.heappush(heap, [end, start])
                    heapq.heappush(heap, [old_end, old_start])
                
            ans = max(ans, len(heap))

            
        return ans
            











        


        
        

        

        