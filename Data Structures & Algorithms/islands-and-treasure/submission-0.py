class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rowLen = len(grid)
        colLen = len(grid[0])

        visited = set()
        q = deque()

        def add_grid(r,c):
            if r < 0 or r >= rowLen or c < 0 or c >= colLen or grid[r][c] == -1 or (r,c) in visited:
                return

            q.append((r,c))
            visited.add((r,c))




        for r in range(rowLen):
            for c in range(colLen):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append((r,c))
        

        dist = 0

        while q:
            for i in range(len(q)):
                r , c  = q.popleft()
                grid[r][c] = dist

                add_grid(r + 1, c)
                add_grid(r - 1, c)
                add_grid(r, c + 1)
                add_grid(r, c - 1)
            
            dist+=1
        









        
        