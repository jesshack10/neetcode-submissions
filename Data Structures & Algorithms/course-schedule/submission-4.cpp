class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        set<int> seen;
        map<int, vector<int>> adj;

        for(const auto& p: prerequisites){
            adj[p[0]].push_back(p[1]);
        }

        unordered_set<int> visited;
        function<bool(int)> dfs = [&](int courseId) -> bool {
            if(seen.count(courseId)) return false;
            if(visited.count(courseId)) return true;

            seen.insert(courseId);
            for(auto const& c: adj[courseId]){
                if(!dfs(c)) return false;
            }
            seen.erase(courseId);
            visited.insert(courseId);
            return true;
        };

        for( int i{}; i < numCourses; i++){
            if(!dfs(i)) return false;
        }

        return true;
    }
};
