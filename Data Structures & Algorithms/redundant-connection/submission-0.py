class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #remove a node, and try to union find, if its sitll a full structure? then it was removable.
        #if its not one structure anymore than we needed it, and try a different node right>


        #one-pass union find, if two nodes already share a parent, than that's the connection taht is redundant
        n = len(edges)

        par = [i for i in range(n+1)]
        rank = [1] * (n+1)

        def find(n1):
            res = n1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
    
            return res

        
        def union(edge):
            n1, n2 = edge

            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1]+=rank[p2]

            
            else:
                par[p1] = p2
                rank[p2] +=rank[p1]
            
            return True

        for edge in edges:
            if union(edge) == False:
                return edge       



        