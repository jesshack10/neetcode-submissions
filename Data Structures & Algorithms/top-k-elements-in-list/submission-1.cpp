class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> bucket(nums.size()+1);
        unordered_map<int, int> freq;
        vector<int> topknums{};

        for(const auto& num:nums){
            freq[num] += 1;
        }

        for(auto [num,f]: freq){
            bucket[f].push_back(num);
        }

        int numssize = nums.size();
        int currk = 0;
        
        for(int i = nums.size(); i >=0; i--){
            for(int bi=0; bi < bucket[i].size(); bi++){
                
                if(topknums.size() == k) return topknums;

                topknums.push_back(bucket[i][bi]);
            }
        }
        return topknums;

    }
};
