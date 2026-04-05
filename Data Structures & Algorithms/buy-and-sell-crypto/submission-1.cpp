class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int currmin{INT_MAX}, currmax{0};
        int maxprofit = 0;
        for(auto price:prices){
            if (price < currmin) {
                currmin = price;
                currmax = price;
            }
            currmax = max(currmax, price);
            maxprofit = max(maxprofit, currmax - currmin);
        }

        return maxprofit;
    }
};
