class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        adj = defaultdict(list)

        for edge in edges:
            source, dst, w = edge

            adj[source].append([dst, w])

        minheap = [[0, src]]

        res = {}


        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in res: 
                continue
            
            res[n1] = w1
            for nei in adj[n1]:
                n2, w2 = nei
                if n2 not in res:
                    heapq.heappush(minheap, [w1 + w2, n2])

        for i in range(n):
            if i not in res:
                res[i] = -1
        return res
        











        





