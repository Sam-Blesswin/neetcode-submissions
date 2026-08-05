class Solution {

    public String encode(List<String> strs) {
        StringBuilder res = new StringBuilder();
        for(String s: strs){
            res.append(s.length()).append("#").append(s);
        }
        return res.toString();
    }

    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int itr = 0;
        while(itr<str.length()){
            int n = 0;
            while(str.charAt(itr) != '#'){
                n = n*10 + (str.charAt(itr) - '0');
                itr++;
            }
            itr++;
            res.add(str.substring(itr, itr+n));
            itr += n;
        }

        return res;
    }
}
