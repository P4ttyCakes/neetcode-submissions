class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        unvisited = set(range(len(points))) # 0 , 1, 2 , 3 , we can acess each point by points[i]

        if len(points) == 0:
            return 0

        total = 0
        shortest = {}

        start = [0,0]

        minHeap = [start]

        while minHeap:
            dist, i = heapq.heappop(minHeap)

            if i in shortest:
                continue
            
            shortest[i] = dist
            total+=dist

            unvisited.remove(i)

            x1, y1 = points[i]

            for i2 in unvisited:
                x2, y2 = points[i2]
                dist2 = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, [dist2, i2])

        
        return total

                
                
            
            
            




        