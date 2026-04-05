class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l{0};
        int minlenght = 1000001;
        int currSum{0};

        for(int r = 0; r < nums.size(); r++){

            currSum += nums[r];

            while(currSum >= target){
                minlenght = min(minlenght, r - l + 1);
                currSum -= nums[l];
                l += 1;
            }
        }

        return (minlenght == 1000001)? 0 : minlenght;
    }
};