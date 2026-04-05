class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> s1,s2;

        for(const auto& c:s)
            s1[c] += 1;

        for(const auto& c:t)
            s2[c] += 1;
        
        for(char letter = 'a'; letter <= 'z'; letter++){
            if(s1[letter] != s2[letter])
                return false;
        }

        return true;
    }
};
