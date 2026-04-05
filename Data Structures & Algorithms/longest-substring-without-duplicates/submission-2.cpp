class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> seen;
        int res{};
        int l{};
        
        for(int r{}; r < s.size(); r++){
            char currchar = s[r];

            if(seen.count(currchar)){
                l = max(l, seen[currchar] + 1);
            }
             res = max(res, r - l + 1);

            seen[currchar] = r;
        }

        return res;
    }
};
