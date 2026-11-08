class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)

        
        def bfs(node):
            queue = deque([])

            queue.append([node,-1, 0])

            while queue:
                node, parent, depth = queue.popleft()

                for nei in adj[node]:
                    if nei == parent:
                        continue
                    queue.append([nei, node, depth+1])

            return depth
        

        res = []
        minim = float('inf')

        for i in range(n):
            height = bfs(i)

            if height < minim:
                res = [i]
                minim = height
            
            elif height == minim:
                res.append(i)
          
        
        return res






        