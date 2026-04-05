class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue minheap(nums.begin(),nums.end(), greater<int>());

        while(minheap.size()>k){
            minheap.pop();
        }

        return minheap.top();
    }
};
