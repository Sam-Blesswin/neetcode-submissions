class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        queue<pair<int,int>> q;

        for(int i=0; i<grid.size(); i++){
            for(int j=0; j<grid[0].size(); j++){
                if(grid[i][j] == 0){
                    q.push({i,j});
                }
            }
        }

        vector<vector<int>> directions = {{-1,0}, {+1,0}, {0,-1}, {0,+1}};
        
        int dist = 0;
        while(!q.empty()){
            int s = q.size();
            dist++;

            for(int i=0; i<s; i++){
                auto data =q.front(); q.pop();
                for(auto dir: directions){
                    int _x = data.first + dir[0];
                    int _y = data.second + dir[1];

                    if(_x<0 || _x>=grid.size() || _y<0 || _y>=grid[0].size()){
                        continue;
                    }

                    if(grid[_x][_y] == INT_MAX){
                        grid[_x][_y] = dist;
                        q.push({_x,_y});
                    }
                }
            }
        }
    }
};
