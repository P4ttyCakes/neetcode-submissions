class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adj = defaultdict(list)

        for src, dst in tickets:
            adj[src].append(dst)

        for airport in adj.keys():
            adj[airport].sort(reverse= True)


        res = []
        
        def dfs(airport):

            while len(adj[airport]) != 0 :
                next_airport = adj[airport].pop()
                dfs(next_airport)
            
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]
        
            
            

            




        