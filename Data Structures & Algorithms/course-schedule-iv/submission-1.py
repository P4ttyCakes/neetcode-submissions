class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        adj = defaultdict(list)

        visited = {}

        for pre, course in prerequisites:
            adj[course].append(pre)
        
        def dfs(pre, course):

            if (pre, course) in visited:
                return visited[(pre, course)]

            if pre == course:
                return True

            for nei in adj[course]:
                if dfs(pre, nei):
                    visited[(pre, course)] = True
                    return True
                
            visited[(pre, course)] = False
            return False

            

        res = []
        for pre, course in queries:
            res.append(dfs(pre, course))

        return res






        