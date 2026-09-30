class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        direction = [(1,0), (-1,0), (0,1), (0,-1)]

        water_level = 0

        shortest = set()

        minHeap = [[grid[0][0], (0,0)]]


        while minHeap:
            dist, (r,c) = heapq.heappop(minHeap)

            if (r,c) in shortest:
                continue

            shortest.add((r,c))

            if r == rows - 1 and c == cols -1:
                return dist


            for dr, dc in direction:
                r2 = r + dr
                c2 =  c + dc

                if 0 <= r2 and r2 < rows and 0 <= c2 and c2 < cols:
                
                    if (r2, c2) not in shortest:
                        heapq.heappush(minHeap, [max(dist, grid[r2][c2]), (r2,c2)])

        return water_level
        
    




            



        