class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = defaultdict(list)
        for src, dst in edges:  
            adj[src].append(dst)
            adj[dst].append(src)
        

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)
            
            for nei in adj[node]:
                if nei == parent:
                    continue

                if dfs(nei, node) == False:
                    return False
                
            return True

        return dfs(0, -1) and len(visited) == n

        