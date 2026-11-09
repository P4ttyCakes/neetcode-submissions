class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #prim's algorithms


        heap = []
        if len(points) == 0:
            return 0 
        unvisited = set(range(len(points)))

        total = 0

        start = [0, 0]
        shortest = {}

        minHeap = [start]

        while minHeap:

            dist, i = heapq.heappop(minHeap)

            if i in shortest:
                continue

            shortest[i] = dist
            total += dist
            unvisited.remove(i)

            x1, y1 = points[i]
            
            for i2 in unvisited:
                x2, y2 = points[i2]
                distance2 = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, [distance2, i2])

        return total













        
        