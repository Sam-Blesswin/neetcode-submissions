class Solution {
private:
    vector<int> parent, rank;

    int find(int n){
        int node = n;
        while(n != parent[n]){
            n = parent[n];
        }
        parent[node] = n;
        return n;
    }

    bool unionSet(int u, int v){
        int pu = find(u);
        int pv = find(v);

        if(pu == pv){
            return false;
        }

        if(rank[pu] >= rank[pv]){
            parent[v] = pu;
            parent[pv] = pu;
            rank[pu] += rank[pv]; 
        }else{
            parent[u] = pv;
            parent[pu] = pv;
            rank[pv] += rank[pu];
        }

        return true;
    }

public:
    int countComponents(int n, vector<vector<int>>& edges) {
        parent = vector<int>(n);
        for(int i=0; i<n; i++){
            parent[i] = i;
        }
        rank = vector<int>(n,1);

        int res = n;
        for(vector<int> edge: edges){
            if(unionSet(edge[0],edge[1])){
                res--;
            }
        }

        return res;
    }
};
