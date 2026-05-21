class Solution {
private:
    unordered_set<int> visited;
    void dfs(vector<vector<int>>& adjList, int u, int parent){
        if(visited.find(u) != visited.end()){
            return;
        }

        visited.insert(u);

        for(auto& v: adjList[u]){
            if(v == parent){
                continue;
            }

            dfs(adjList, v, u);
        }
    }
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList(n);
        for(auto& edge: edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }   

        int res = 0;
        for(int i=0; i<n; i++){
            if(visited.find(i) == visited.end()){
                res++;
                dfs(adjList, i, -1);
            }
        }

        return res;
    }
};
