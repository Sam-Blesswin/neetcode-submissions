class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific, atlantic = set(), set()
        r = len(heights)
        c = len(heights[0])

        def dfs(i,j,prev,visited):
            if (i,j) in visited or i<0 or j<0 or i>=r or j>=c:
                return
            if heights[i][j] < prev:
                return
            visited.add((i,j))
            dfs(i-1,j,heights[i][j], visited)
            dfs(i+1,j,heights[i][j], visited)
            dfs(i,j-1,heights[i][j], visited)
            dfs(i,j+1,heights[i][j], visited)
        
        for j in range(c):
            dfs(0,j,-1,pacific)
            dfs(r-1,j,-1,atlantic)
        
        for i in range(r):
            dfs(i,0,-1,pacific)
            dfs(i,c-1,-1,atlantic)

        res = []
        for i in range(r):
            for j in range(c):
                if (i,j) in pacific and (i,j) in atlantic:
                    res.append([i,j])
        return res




        