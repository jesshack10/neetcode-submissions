class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {

        int ROWS = board.size();
        int COLS = board[0].size();
        std::set<std::pair<int,int>> path;

        std::function<bool(int, int, int)> searchWord = [&](int i, int r, int c) -> bool{ 
            
            if (i == word.size()){
                return true;
            }

            if(r < 0 or r >= ROWS || c < 0 or c >= COLS || board[r][c]!=word[i] || path.count({r,c})){
                return false;
            }

            
            
            path.insert({r,c});
            bool res = searchWord(i + 1, r - 1, c) || 
                    searchWord(i + 1, r + 1, c) || 
                    searchWord(i + 1, r, c + 1) || 
                    searchWord(i + 1, r, c - 1);
            path.erase({r,c});
            return res;
        };

        for(int r = 0; r < ROWS; r ++){
            for(int c = 0; c < COLS; c++){
                
                if(board[r][c] == word[0]){
                    if (searchWord(0, r, c)){
                        return true;
                    }
                }
            }
        }

        return false;
    }
};
