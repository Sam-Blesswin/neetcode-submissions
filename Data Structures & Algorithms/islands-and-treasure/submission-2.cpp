class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        queue<pair<int,int>> queue;

        int m = grid.size();
        int n = grid[0].size();

        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j] == 0){
                    queue.push({i,j});
                }
            }
        }

        int dist = 0;
        while(!queue.empty()){
            int s = queue.size();
            dist++;

            for(int i=0; i<s; i++){
                auto& coord = queue.front();
                queue.pop();

                int x = coord.first;
                int y= coord.second;

                if(x-1>=0 && grid[x-1][y] == INT_MAX){
                    grid[x-1][y] = dist;
                    queue.push({x-1,y});
                }
                if(x+1<m && grid[x+1][y] == INT_MAX){
                    grid[x+1][y] = dist;
                    queue.push({x+1,y});
                }
                if(y-1>=0 && grid[x][y-1] == INT_MAX){
                    grid[x][y-1] = dist;
                    queue.push({x,y-1});
                }
                if(y+1<n && grid[x][y+1] == INT_MAX){
                    grid[x][y+1] = dist;
                    queue.push({x,y+1});
                }
            }
        }
    }
};
