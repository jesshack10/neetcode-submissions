class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size());
        dp[s.size()] = true;
        vector<string> wordbreaks;

        for(int i = s.size(); i >= 0; i--){

            for(auto word: wordDict){
                
                if( i + word.size() <= s.size() && s.substr(i,word.size())==word){
                    dp[i] = dp[i+word.size()];
                    wordbreaks.push_back(word);
                }

                if(dp[i]){
                    break;
                }
            }
        }


        /*for(auto w:wordbreaks){
            cout<<w<<endl;
        }*/
        return dp[0];

    }
};
