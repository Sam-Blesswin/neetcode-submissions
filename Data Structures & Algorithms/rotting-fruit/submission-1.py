class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
        

        dir = [[-1,0],[1,0],[0,1],[0,-1]]
        while q:
            s = len(q)
            for i in range(s):
                plot = q.popleft()
                for d in dir:
                    x = plot[0] + d[0]
                    y = plot[1] + d[1]
                    if x>=0 and x<len(grid) and y>=0 and y<len(grid[0]):
                        if grid[x][y] == 1:
                            q.append([x,y])
                            grid[x][y] = 2
            time+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
                    
        return time-1 if time else 0


