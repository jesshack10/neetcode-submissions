#include <array>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<array<int,26>, vector<string>> anagrams;

        for(const auto& word: strs){
            
            array<int, 26> letterfreq{};
            for(const auto& letter: word){
                letterfreq[letter - 'a'] += 1;
            }

            anagrams[letterfreq].push_back(word);
        }

        vector<vector<string>> groupedanagrams;

        for(const auto& kv: anagrams){
            groupedanagrams.push_back(move(kv.second));
        }


        return groupedanagrams;
    }
};