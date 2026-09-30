class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        max_time = 0

        adj = defaultdict(list)

        for src, dst, time in times:
            adj[src].append([dst,time])

        
        shortest = {}


        
        minHeap = [[0,k]]

        while minHeap:
            time, dst = heapq.heappop(minHeap)
            if dst in shortest:
                continue
            
            shortest[dst] = time
            max_time = max(time, max_time)

            for nei in adj[dst]:
                dst2, time2 = nei
                if dst2 not in shortest:
                    heapq.heappush(minHeap, [time + time2, dst2])


        for i in range(1,n +1):
            if i not in shortest:
                return -1

        return max_time




        
        