class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indexes;

        for(int i{}; i <= nums.size(); i++){

            int currnum = nums[i];
            int num2look = target - currnum;
            if(indexes.count(num2look)) {
                return {indexes[num2look], i};
            }

            indexes[currnum]= i;
        }

        return {};
    }
};
