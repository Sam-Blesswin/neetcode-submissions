class Solution {
private:
    unordered_map<char, vector<char>> adjList;
    unordered_set<char> visited;
    unordered_set<char> pathVisited;
    vector<char> res;

    bool isCycle(char u){
        if(visited.count(u) && pathVisited.count(u)){
            return true;
        }

        if(visited.count(u)){
            return false;
        }

        visited.insert(u);
        pathVisited.insert(u);

        for(auto& v: adjList[u]){
            if(isCycle(v)){
                return true;
            }
        }

        //post order traversal : Hierholzer's Algorithm
        res.push_back(u);

        pathVisited.erase(u);

        return false;
    }

public:
    string foreignDictionary(vector<string>& words) {
        for(auto& word: words){
            for(auto& ch: word){
                adjList[ch] = {};
            }
        }

        for(int i=0; i<words.size()-1; i++){
            string& a = words[i];
            string& b = words[i+1];

            int minLen = min(a.length(), b.length());

            if(a.substr(0,minLen) == b.substr(0,minLen)){
                if(a.length() > b.length()){
                    return "";
                }
            }

            for(int j=0; j<a.length(); j++){
                if(a[j] != b[j]){
                    adjList[a[j]].push_back(b[j]);
                    break;
                }
            }
        } 

        //cycle detection
        for(auto& pair :adjList){
            if(visited.count(pair.first)){
                continue;
            }
            
            if(isCycle(pair.first)){
                return "";
            }
        }

        //Hierholzer's Algorithm
        reverse(res.begin(), res.end());

        string order = "";
        for(char ch: res){
            order+=ch;
        }

        return order;
    }
};
