class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for(string& word: strs){
            encoded += to_string(word.length()) +"#" +word;
        }

        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int itr = 0;

        while(itr<s.length()){
            int len = 0;
            while(s[itr] != '#'){
                len = len*10 + (s[itr] - '0');
                itr++;
            }
            res.push_back(s.substr(itr+1, len));
            itr += len+1;
        }

        return res;
    }
};
