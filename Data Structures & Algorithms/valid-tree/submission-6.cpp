class Solution {
private:
    bool isCycle(vector<vector<int>>& adjList, unordered_set<int>& visited, int u, int parent){
        if(visited.find(u) != visited.end()){
            return true;
        }

        visited.insert(u);

        for(auto& v: adjList[u]){
            if( v == parent){
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

        for(auto& edge: edges){
            adjList[edge[0]].push_back(edge[1]);
            adjList[edge[1]].push_back(edge[0]);
        }
        
        unordered_set<int> visited;

        if(isCycle(adjList, visited, 0, -1)){
                return false;
        }
        
        for(int i=0; i<n; i++){
            if(visited.find(i) == visited.end()){
                return false;
            }
        }

        return true;
    }
};
