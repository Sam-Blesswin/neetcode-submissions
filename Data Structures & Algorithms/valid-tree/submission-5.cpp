class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList(n);

        for(auto& edge: edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        queue<pair<int,int>> queue;

        queue.push({0,-1});

        unordered_set<int> visited;

        while(!queue.empty()){
            auto& pair = queue.front();
            int u = pair.first;
            int parent = pair.second;

            queue.pop();

            if(visited.find(u) != visited.end()){
                return false;
            }

            visited.insert(u);

            for(auto& v: adjList[u]){
                if(v == parent){
                    continue;
                }
                queue.push({v,u});
            }
        }

        return visited.size() == n;
    }
};
