class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits: return []
        keymap = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y", "z"],
        }
        words = []
        def dfs(i, currPath):
            if i == len(digits):
                words.append(currPath)
                return
            
            
            for l in keymap[digits[i]]:
                dfs(i + 1, currPath + l)
            
        dfs(0,"")

        return words
            