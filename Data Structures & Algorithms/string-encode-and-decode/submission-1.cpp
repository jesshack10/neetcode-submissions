class Solution {
public:

    string encode(vector<string>& strs) {

        if(strs.empty()) return "";
        string encodedstr{};

        for(auto word:strs){
            string size = std::to_string(word.size());
            encodedstr += size + "#" + word;
        }

        return encodedstr;
    }

    vector<string> decode(string s) {
        if(s.empty()) return {};
        int curri = 0;
        vector<string> decodedstr;

        while(curri < s.size()){

            string wordsize = "";
            while(s[curri] != '#'){
                wordsize += s[curri];
                //cout<<"wordsize:"<<wordsize<<endl;
                curri++;
            }
            int wordlen = std::stoi(wordsize);
            decodedstr.push_back(s.substr(curri + 1, wordlen));

            curri += (wordlen + 1);
        }

        return decodedstr;
    }
};
