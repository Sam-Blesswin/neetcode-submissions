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

    void unionFind(int u, int v){
        int pu = find(u);
        int pv = find(v);

        if(rank[pu] >= rank[pv]){
            parent[v] = pu;
            parent[pv] = pu;
            rank[pu] += rank[pv]; 
        }else{
            parent[u] = pv;
            parent[pu] = pv;
            rank[pv] += rank[pu];
        }
    }

public:
    int countComponents(int n, vector<vector<int>>& edges) {
        parent = vector<int>(n);
        for(int i=0; i<n; i++){
            parent[i] = i;
        }
        rank = vector<int>(n,1);

        for(vector<int> edge: edges){
            unionFind(edge[0],edge[1]);
        }

        for(vector<int> edge: edges){
            parent[edge[0]] = find(edge[0]);
            parent[edge[1]] = find(edge[1]);
        }

        unordered_set<int> set;
        for(int i=0; i<n; i++){
            set.insert(parent[i]);
        }

        return set.size();
    }
};
