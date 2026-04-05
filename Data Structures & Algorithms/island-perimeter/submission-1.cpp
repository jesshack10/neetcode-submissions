class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {

        int ROWS = grid.size();

        int COLS = grid[0].size();

        set<pair<int,int>> visited;

        function<int(int, int)> dfs = [&](int r, int c)->int{

            pair<int,int> currpair(r,c);

            if(r < 0 || r >=ROWS || c<0||c>= COLS || grid[r][c]==0) return 1;

            if(visited.count(currpair)){
                return 0;
            }

            visited.insert(currpair);

            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1);

        };

        for(int i{0}; i<ROWS; i++){
            for(int j{0}; j<COLS; j++){
                if(grid[i][j] == 1){
                    return dfs(i,j);
                }
            }
        }

        return 0;

    }
};