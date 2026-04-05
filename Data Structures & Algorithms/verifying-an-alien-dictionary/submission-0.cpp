class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        map<char, int> ordermap;
        int idx = 0;
        for(auto c: order){
            ordermap[c] = idx++;
        }

        for(int i{0}; i < (words.size() - 1); i++){
            string firstw = words[i];
            string secondw = words[i+1];
            for(int idx{0}; idx < firstw.size(); idx++){
                if (idx == secondw.size()) return false;
                if(firstw[idx]!=secondw[idx]){
                    if(ordermap[firstw[idx]] > ordermap[secondw[idx]]){
                        return false;
                    }
                    break;
                }
            }
            
        }
        return true;
    }
};