class Solution {
public:

    string encode(vector<string>& strs) {
        string hash = "";
        for(string& str: strs){
            hash += to_string(str.length())+"#"+str;
        }
        return hash;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int itr = 0;

        while(itr < s.length()){
            int num=0;
            while(s[itr] != '#'){
                num = num * 10 + (s[itr] - '0');
                itr++;
            }
            itr++;
            res.push_back(s.substr(itr, num));
            itr += num;
        }

        return res;
    }
};
