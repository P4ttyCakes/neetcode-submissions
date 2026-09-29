class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        rows = len(heights)
        cols = len(heights[0])

        minHeap = [[0, (0,0)]]

        shortest = {}


        #the weights of each traversal is the just the difference in height


        directions = [(0,1), (0,-1), (1,0), (-1,0)]



        while minHeap:

            w1, (r,c) = heapq.heappop(minHeap)
            if (r,c) in shortest:
                continue
            
            shortest[(r,c)] = w1

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr and  nr < rows and 0 <= nc and nc < cols:
                    if (nr,nc) not in shortest:
                        heapq.heappush(minHeap, [max(w1 , abs(heights[nr][nc] - heights[r][c])), (nr,nc)])
        
        return shortest[(rows-1, cols - 1)]


        















        






        



        








        