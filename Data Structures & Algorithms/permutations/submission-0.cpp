class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        return permute_helper(0,nums);
    }

    vector<vector<int>> permute_helper(int i, vector<int>& nums){
        if (i == nums.size()){
            return {{}};
        }

        vector<vector<int>> perms = permute_helper(i + 1, nums);
        vector<vector<int>> res;
        for(auto perm : perms){
            for(int j = 0 ; j <= perm.size(); j++){
                vector<int> p_copy = perm;
                p_copy.insert(p_copy.begin() + j, nums[i]);
                res.push_back(p_copy);
            }
        }

        return res;
    }
};
