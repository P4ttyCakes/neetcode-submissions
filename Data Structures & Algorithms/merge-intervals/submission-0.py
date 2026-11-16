class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()


        stack = []

        for i in range(len(intervals)):
            start, end = intervals[i]

            if not stack:
                stack.append([start,end])

            #check if it needs to be merged
            else:
                prev_start, prev_end = stack[-1]
                if start <= prev_end:
                    stack.pop()
                    stack.append([min(start, prev_start), max(end, prev_end)])
                
                else:
                    stack.append([start,end])
        
        return stack


            


        