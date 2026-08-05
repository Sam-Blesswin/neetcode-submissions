class Solution {
private:
    vector<int> parent;
    vector<int> rank;

    int find(int n){
        int node = n;
        while(n != parent[n]){
            n = parent[n];
        }

        parent[node] = n;
        return n;
    }

    bool unionRank(int u, int v){
        int pu = find(u);
        int pv = find(v);

        if(pu == pv){
            return false;
        }

        if(rank[pu] >= rank[pv]){
            parent[pv] = pu;
            parent[v] = pu;
            rank[pu] += rank[pv];

        }else{
            parent[pu] = pv;
            parent[u] = pv;
            rank[pv] += rank[pu];
        }

        return true;
    }

public:
    bool validTree(int n, vector<vector<int>>& edges) {
        parent = vector<int>(n);
        for(int i=0; i<n; i++){
            parent[i] = i;
        }
        rank = vector<int>(n, 1);

        for(vector<int>& edge: edges){
            if(!unionRank(edge[0], edge[1])){
                return false;
            }
        }

        for(vector<int>& edge: edges){
            int u = edge[0];
            int v = edge[1];

            parent[u] = find(u);
            parent[v] = find(v);
        }

        for(int i=0; i<n-1; i++){
            if(parent[i] != parent[i+1]){
                return false;
            }
        }

        return true;
    }
};
