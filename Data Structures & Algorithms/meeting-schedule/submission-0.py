"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sorting and then looping forward seeing if we start, touches the previous's end
        intervals.sort(key= lambda x: x.end)

        prev_end = None

        for interval in intervals:
            start = interval.start
            end = interval.end

            if prev_end is None:
                prev_end = end

            else:
                if start < prev_end:
                    return False
                
                prev_end = end
        
        return True



