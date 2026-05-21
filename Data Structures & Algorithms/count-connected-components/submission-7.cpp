class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList(n);

        for(auto& edge: edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        queue<pair<int,int>> queue;
        unordered_set<int> visited;
        int res = 0;

        for(int i=0; i<n; i++){
            if(visited.find(i) != visited.end()){
                continue;
            }
            
            res++;
            queue.push({i,-1});

            while(!queue.empty()){
                auto& pair = queue.front();
                int u = pair.first;
                int parent = pair.second;
                queue.pop();

                if(visited.find(u) != visited.end()){
                    continue;
                }

                visited.insert(u);

                for(auto& v: adjList[u]){
                    if(v == parent){
                        continue;
                    }
                    queue.push({v,u});
                }
            }
        }

        return res;
    }
};
