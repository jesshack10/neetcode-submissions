class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0, r = heights.size() - 1;
        int maxwater = 0;
        while(l < r) {
            int hleft = heights[l];
            int hright = heights[r];
            int currwater = (r - l) * min(hleft, hright);
            maxwater = max(maxwater, currwater);

            if(hleft > hright) r--;
            else l++;
        }

        return maxwater;
    }
};
