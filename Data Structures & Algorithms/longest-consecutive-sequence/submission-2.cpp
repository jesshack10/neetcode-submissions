class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res{};
        unordered_set<int> seen;

        for(const auto& num: nums){
            seen.insert(num);
        }

        for(const auto& num:seen){

            if(!seen.count(num - 1)){
                int search_num = num;
                int lenght = 0;
                while(seen.count(search_num)){
                    search_num++;
                    lenght++;
                }
                res = max(res, lenght);
            }

        }

        return res;
    }
};
