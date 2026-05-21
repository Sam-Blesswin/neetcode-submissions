class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        queue<vector<int>> queue;

        for(int i=0; i<grid.size(); i++){
            for(int j=0; j<grid[0].size(); j++){
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
                vector<int> coord = queue.front();
                queue.pop();
                int x = coord[0];
                int y = coord[1];

                if(x-1 >=0 && grid[x-1][y] == INT_MAX){
                    grid[x-1][y] = dist;
                    queue.push({x-1,y});
                }
                if(x+1 < grid.size() && grid[x+1][y] == INT_MAX){
                    grid[x+1][y] = dist;
                    queue.push({x+1,y});
                }
                if(y-1 >=0 && grid[x][y-1] == INT_MAX){
                    grid[x][y-1] = dist;
                    queue.push({x,y-1});
                }
                if(y+1 < grid[0].size() && grid[x][y+1] == INT_MAX){
                    grid[x][y+1] = dist;
                    queue.push({x,y+1});
                }
            }
        }
    }
};
