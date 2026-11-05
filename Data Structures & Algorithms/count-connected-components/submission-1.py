class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n


        def find(n):
            res = n
            while res != par[res]:
                res = par[res]
            
            return res
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            
            #case where union needs to happen

            if rank[p1] > rank[p2]:
                rank[p1]+=1
                par[p2] = p1
            
            else:
                rank[p2]+=1
                par[p1] = p2
            
            return 1

        connected = n
        for n1, n2 in edges:
            connected -= union(n1,n2)
        
        return connected
        

                





            


        