class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList(n);

        for(auto& edge: edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        unordered_set<int> visited;

        queue<pair<int,int>> q;
        q.push({0,-1});
    
        while(!q.empty()){
            auto& data = q.front();
            int u = data.first;
            int parent = data.second;
            q.pop();

            if(visited.find(u) != visited.end()){
                return false;
            }

            visited.insert(u);

            for(int v: adjList[u]){
                if(v == parent){
                    continue;
                }
                q.push({v,u});
            }
        }

        return visited.size() == n;
    }
};
