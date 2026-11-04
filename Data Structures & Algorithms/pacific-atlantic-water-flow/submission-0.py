class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        if rows == 0:
            return []


        #pacific checks

        pacific = set()
        atlantic = set()
        directions = ((0,1), (0,-1), (1,0), (-1,0))

        def flow(r,c, ocean):

            if (r,c) in ocean:
                return
            
            ocean.add((r,c))



            if 0 <= r< rows and 0 <= c < cols:
                for dr,dc in directions:
                    if (r + dr,c + dc) not in ocean and 0 <= dr + r< rows and 0 <= dc +c < cols and heights[r][c] <= heights[r +dr][c + dc]:

                        flow(dr + r,dc + c, ocean)
                        

        for i in range(rows):
            flow(i,0, pacific)
        
        for i in range(cols):
            flow(0,i,pacific)


        for i in range(rows):
            flow(i ,cols - 1, atlantic)

        for i in range(cols):
            flow(rows - 1, i,atlantic)

        
        res = []
        for r,c in pacific:
            if (r,c) in atlantic:
                res.append((r,c))

        return res

        #check the bottomr row, and right-side for 