class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        queue<pair<int,int>> queue;

        for(int i=0; i<grid.size(); i++){
            for(int j=0; j<grid[0].size(); j++){
                if(grid[i][j] == 0){
                    queue.push({i,j});
                }
            }
        }

        int dist = 0;
        vector<vector<int>> directions = {{-1,0}, {1,0}, {0,-1},{0,1}};
        while(!queue.empty()){
            int s = queue.size();
            dist++;

            for(int i=0; i<s; i++){
                auto& coord = queue.front();
                int x = coord.first;
                int y = coord.second;

                queue.pop();

                for(auto& dir: directions){
                    int i = x + dir[0];
                    int j = y + dir[1];

                    if(i<0 || i>=grid.size() || j<0 || j>= grid[0].size()){
                        continue;
                    }

                    if(grid[i][j] == INT_MAX){
                        grid[i][j] = dist;
                        queue.push({i,j});
                    }
                }
            }
        }
    }
};
