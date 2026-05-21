class Solution {
private:
    bool isCycle(vector<vector<int>>& adjList,vector<bool>& visited, int u, int parent){
        if(visited[u]){
            return true;
        }

        visited[u] = true;

        for(auto& v: adjList[u]){
            if(v == parent){
                continue;
            }
            if(isCycle(adjList, visited, v, u)){
                return true;
            }
        }

        return false;
    }
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        vector<vector<int>> adjList(n);
        vector<bool> visited(n);

        for(auto& edge: edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }

        if(isCycle(adjList, visited, 0, -1)){
            return false;
        }

        for(int i=0; i<visited.size(); i++){
            if(!visited[i]){
                return false;
            }
        }

        return true;
    }
};
