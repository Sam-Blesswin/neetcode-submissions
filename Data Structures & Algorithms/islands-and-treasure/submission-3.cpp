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

        vector<pair<int,int>> directions = {{-1,0},{1,0},{0,-1},{0,1}};

        int dist = 0;
        while(!queue.empty()){
            int s = queue.size();
            dist++;

            for(int i=0; i<s; i++){
                auto& coord = queue.front();
                queue.pop();

                int x = coord.first;
                int y= coord.second;

                for(auto& dir: directions){
                    int _x = x + dir.first;
                    int _y = y + dir.second;

                    if(_x >=0 && _x<m && _y>=0 && _y<n && grid[_x][_y]==INT_MAX){
                        grid[_x][_y] = dist;
                        queue.push({_x,_y});
                    }
                }
            }
        }
    }
};
