class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        queue = []

        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        
        visited = defaultdict(int)
        heapq.heappush(queue, [0, (0,0)])

        while queue:
            
            [dist, (r,c)] = heapq.heappop(queue)

            if (r,c) in visited:
                continue
            
            visited[(r,c)] = dist

            for dr, dc in directions:

                new_row = dr + r
                new_col = dc + c

                if 0 <= new_row < len(heights) and 0 <= new_col < len(heights[0]) and (new_row, new_col)not in visited:

                    dist_calc = abs(heights[r][c] - heights[new_row][new_col])

                    heapq.heappush(queue, [max(visited[(r,c)] , dist_calc), (new_row, new_col)])
        
        return visited[(len(heights) -1 , len(heights[0]) -1)]


            


        