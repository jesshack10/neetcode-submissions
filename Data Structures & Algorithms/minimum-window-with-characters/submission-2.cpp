class Solution {
public:
    string minWindow(string s, string t) {
        
        if(t=="") return "";

        unordered_map<char, int> window, goal;
        for(auto c:t){
            goal[c] += 1;
        }

        int have{0};
        int want = goal.size();
        int l{0};
        int minL = s.size()+1;
        pair<int,int> winindexes{0,0};

        for(int r = 0; r < s.size(); r++){
            //add the character to the window map
            char currchar = s[r];
            window[currchar] += 1;

            if(goal.count(currchar) && window[currchar] == goal[currchar]){
                have++;
            }
            //I want to run this WHILE they are equal, because that means i can shrink the window
            // and still satisfy the requirements
            while(have == want){
                //save the result
                if(r-l+1 < minL){
                    winindexes={l,r};
                    minL = r-l+1;
                }

                //shrink the window from left
                char firstchar = s[l];
                l++;
                window[firstchar]--;

                if(goal.count(firstchar) && window[firstchar] < goal[firstchar]){
                    have--;
                }
            }
        }

        return ( minL == s.size() + 1)? "" : s.substr(winindexes.first, minL);
    }
};
