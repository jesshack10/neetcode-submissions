class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string longestprefix = "";
        bool sameprefix{true};
        int index =0;
        while (index < strs[0].size()){
  
            int currprefix=strs[0][index];
            for(auto word:strs){
                if(word[index]!=currprefix){
                    return longestprefix;
                }
            }
            longestprefix+=currprefix;
            index++;
        }

        return longestprefix;
    }
};