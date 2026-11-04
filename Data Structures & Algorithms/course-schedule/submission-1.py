class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        adj = defaultdict(list)

        for course, pre in prerequisites:
            adj[course].append(pre)

        
        visited = set()
        completed = set()
        def dfs(course):

            if course in visited:
                return False
            
            if course in completed:
                return True
            
            visited.add(course)
            for pre in adj[course]:
                
                if dfs(pre) == False:
                    return False

            visited.remove(course)
            completed.add(course)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        
        return True
