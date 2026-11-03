class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])


        #bfs from every end_point

        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append([row,col])

        distance = 0
        seen = set()

        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        while queue:
            for i in range(len(queue)):

                r,c = queue.popleft()

                if (r,c) in seen:
                    continue

                




                

                if distance < grid[r][c]:
                    grid[r][c] = distance
                
                for r_off, c_off in directions:
                    dr = r + r_off
                    dc = c + c_off

                    if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] != -1 and (dr,dc) not in seen:
                        queue.append([dr,dc])
                        seen.add((r,c))
            
            distance+=1
                
                


        
                



                    
        