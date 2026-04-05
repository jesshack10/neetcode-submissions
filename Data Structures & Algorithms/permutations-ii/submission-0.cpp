class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        return permunique_helper(0, nums);
    }

    vector<vector<int>> permunique_helper(int i, vector<int>& nums){
        if(i == nums.size()){
            return {{}};
        }

        vector<vector<int>> perms = permunique_helper(i+1,nums);
        set<vector<int>> uniques;
        for(auto perm: perms){
            for(int j = 0; j<=perm.size(); j++){
                vector<int> p_copy = perm;
                p_copy.insert(p_copy.begin() + j, nums[i]);
                uniques.insert(p_copy);
            }
        }

        vector<vector<int>> res;
        for(auto unique : uniques){
            res.push_back(unique);
        }
        return res;
    } 
};