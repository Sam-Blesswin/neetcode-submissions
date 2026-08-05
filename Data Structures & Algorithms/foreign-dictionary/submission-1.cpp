class Solution {
private:
    unordered_map<char, vector<char>> adjList;
    unordered_map<char, bool> visited;
    unordered_map<char, bool> pathVisited;
    vector<char> res;

    bool isCycle(char ch){
        if(visited[ch] && pathVisited[ch]){
            return true;
        }

        if(visited[ch]){
            return false;
        }

        visited[ch] = true;
        pathVisited[ch] = true;

        for(char next: adjList[ch]){
            if(isCycle(next)){
                return true;
            }
        }

        res.push_back(ch);
        pathVisited[ch] = false;
        return false;
    }

public:
    string foreignDictionary(vector<string>& words) {
        for(string& word: words){
            for(char ch: word){
                adjList[ch];
            }
        }
        
        for(int i=0; i<words.size()-1; i++){
            string& a = words[i];
            string& b = words[i+1];

            int minLen = min(a.length(), b.length());

            if((a.substr(0,minLen) == b.substr(0,minLen))
                && (a.length() > b.length())){
                    return "";
            }



            for(int i=0; i<a.length(); i++){
                if(a[i] != b[i]){
                    adjList[a[i]].push_back(b[i]);
                    break;
                }
            }
        }

        for(auto& pair: adjList){
            if(isCycle(pair.first)){
                return "";
            }
        }

        reverse(res.begin(),res.end());

        string order = "";
        for(char ch: res){
            order += ch;
        }

        return order;
    }
};
