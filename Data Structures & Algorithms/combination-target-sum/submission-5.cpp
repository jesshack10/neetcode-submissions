class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        res.clear();
        currnums.clear();
        currsum = 0;
        backtrack(0, nums, target);

        return res;
    }

    void backtrack(int i, vector<int>& nums, int target){
        if(currsum == target){
            res.push_back(currnums);
            return;
        }
        if(i >= nums.size() || currsum > target){
            return;
        }

        currnums.push_back(nums[i]);
        currsum+=nums[i];
        backtrack(i,nums,target);

        currnums.pop_back();
        currsum-=nums[i];
        backtrack(i + 1,nums, target);
    }

    int currsum{0};
    vector<vector<int>> res;
    vector<int> currnums;
};
