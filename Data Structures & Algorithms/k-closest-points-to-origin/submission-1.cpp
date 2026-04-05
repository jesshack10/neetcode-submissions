class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> closestm;

        for(const auto& point:points){
            int x2 = point[0];
            int y2 = point[1];
            int distance =  x2 * x2 + y2 * y2;
            closestm.push({distance, point});
            if(closestm.size()>k){
                closestm.pop();
            }
        }

        vector<vector<int>> v;
        while(!closestm.empty()){
            v.push_back(closestm.top().second);
            closestm.pop();
        }

        return v;
    }
};
