class Solution {
private:
    unordered_set<int> visited;

    bool isCycle(vector<vector<int>>& adjList, int u, int parent){
        if(visited.find(u) != visited.end()){
            return true;
        }

        visited.insert(u);

        for(auto& v: adjList[u]){
            if(v == parent){
                continue;
            }

            if(isCycle(adjList,v, u)){
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

        if(isCycle(adjList, 0, -1)){
            return false;
        }

        return visited.size() == n;
    }
};
