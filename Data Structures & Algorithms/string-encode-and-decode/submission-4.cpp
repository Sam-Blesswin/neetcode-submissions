class Solution {
public:

    string encode(vector<string>& strs) {
        string encode = "";
        for(auto& str: strs){
            encode+= to_string(str.length()) + "#" + str;
        }
        return encode;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int itr = 0;

        while(itr < s.length()){
            int n = 0;
            while(s[itr] != '#'){
                n = n*10 + (s[itr] - '0');
                itr++;
            }
            itr++;
            res.push_back(s.substr(itr, n));
            itr+=n;
        }

        return res;
    }
};
