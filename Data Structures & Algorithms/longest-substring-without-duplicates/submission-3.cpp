class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char,int> seen;
        int res{};
        int l{};

        for(int r{}; r < s.size(); r++){
            if(seen.count(s[r])){
                l = max(l, seen[s[r]] + 1);
            }
            res = max (res, r - l + 1);

            seen[s[r]] = r;
        }
        
        return res;
    }
};
