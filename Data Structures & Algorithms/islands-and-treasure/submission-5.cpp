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

        int dist = 0;

        vector<vector<int>> direction = {{-1,0}, {1,0}, {0,-1}, {0,1}};

        while(!q.empty()){
            int s = q.size();

            dist++;

            for(int i=0; i<s; i++){
                auto& coord = q.front();
                int x = coord.first;
                int y = coord.second;

                q.pop();

                for(auto& dir: direction){
                    int _x = x + dir[0];
                    int _y = y + dir[1];

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
