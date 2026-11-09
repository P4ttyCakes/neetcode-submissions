class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for src,dst,time in times:
            adj[src].append([time,dst])

        queue = []
        visited = defaultdict(int)
        max_time = 0

        heapq.heappush(queue, [0, k])

        while queue:

            distance, node = heapq.heappop(queue)

            if node in visited: 
                continue

            visited[node] = distance
            max_time = max(distance, max_time)

            for nei_distance, nei in adj[node]:
                heapq.heappush(queue, [nei_distance + distance, nei])


        if len(visited) != n:
            return -1 
        return max_time 

        

            
            







        