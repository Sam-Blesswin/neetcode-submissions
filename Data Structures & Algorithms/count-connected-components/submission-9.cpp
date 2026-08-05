class Solution {
private:
    void dfs(vector<vector<int>>& adjList, vector<bool>& visited, int u, int parent){
        if(visited[u]){
            return;
        }

        visited[u] = true;

        for(auto& v: adjList[u]){
            if(v == parent){
                continue;
            }
            dfs(adjList, visited, v, u);
        }
    }
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList(n);
        vector<bool> visited(n);

        for(auto& edge: edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        int res = 0;
        for(int i=0 ;i<n; i++){
            if(!visited[i]){
                res++;
                dfs(adjList, visited, i, -1);
            }
        }

        return res;
    }
};
