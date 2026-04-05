class Solution {
public:
    bool isValid(string s) {
        stack<char> symbols;
        map<char,char> symbolmap = {
            {'[', ']'},
            {'{', '}'},
            {'(', ')'}
        };

        for(const auto& c : s){
            if(c=='[' || c=='{' || c=='(') {
                symbols.push(c);
            } else {
                if (symbols.empty() || c != symbolmap[symbols.top()]) {
                    return false;
                }
                symbols.pop();
            }
        }

        return symbols.empty();
    }
};
