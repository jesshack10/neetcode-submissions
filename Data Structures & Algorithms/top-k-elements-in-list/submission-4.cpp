class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        priority_queue<pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>> minheap;
        unordered_map<int,int> freqmap;

        for(const auto& num:nums){
            freqmap[num] += 1;
        }

        for(const auto& [num, freq]: freqmap){
            minheap.push({freq, num});
            
            if(minheap.size() > k)
                minheap.pop();
        }

        vector<int> res;
        while(minheap.size()) {
            res.push_back(minheap.top().second);
            minheap.pop();
        }
        return res;
    }
};
