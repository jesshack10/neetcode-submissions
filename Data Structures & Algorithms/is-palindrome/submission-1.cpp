class Solution {
public:
    bool isPalindrome(string s) {
        string cleanstr;

        for(int i = 0; i < s.size(); i++){
            if(std::isalnum(s[i])){
                cleanstr+=std::tolower(s[i]);
            }
        }
        int l{},r{cleanstr.size() - 1};
        while(l < r){
            if(cleanstr[l] != cleanstr[r]) return false;
            l++;
            r--;
        }

        return true;

    }
};
