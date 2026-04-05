class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> stones_weight;

        for(auto const& stone: stones){
            stones_weight.push(stone);
        }

        while(stones_weight.size() > 1){
            int y = stones_weight.top(); 
            stones_weight.pop(); 
            int x = stones_weight.top();
            stones_weight.pop();

            if(x == y) continue;

            if(x < y)
                stones_weight.push(y-x);

        }
        return stones_weight.empty() ? 0 : stones_weight.top();
    }
};
