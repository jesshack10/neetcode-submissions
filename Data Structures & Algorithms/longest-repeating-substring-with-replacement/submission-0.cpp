class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char,int> seen;
        int l = 0;
        int res = 0;
        for(int r = 0; r < s.size(); r++){
            seen[s[r]] += 1;

            while((r - l + 1) - getMaxValue(seen) > k){
                seen[s[l]]--;
                l++;
            }

            res = max(res, r - l + 1);
        }
        return res;
    }

    int getMaxValue(unordered_map<char,int>& m){
        int maxv = 0;
        for(auto [k,v] : m){
            maxv = max(maxv, v);
        }

        return maxv;
    }
};
