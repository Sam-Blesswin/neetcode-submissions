class Solution {
public:

    string encode(vector<string>& strs) {
        string encoded = "";
        for(string word: strs){
            encoded += to_string(word.length()) + "#" +word;
        }
        cout<<encoded;
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int itr = 0;
        while(itr < s.length()){
            string num = "";
            while(s[itr] != '#'){
                num += s[itr];
                itr++;
            }

            itr++;
            res.push_back(s.substr(itr, stoi(num)));
            itr += stoi(num);
        }
        return res;
    }
};
