class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = defaultdict(list)
        for word in strs:
            warr = [0] * 26
            for c in word:
                #built the map of the word
                warr[ord(c) - ord('a')] += 1

            #add the word to itrs corresponding space in map
            anagramMap[tuple(warr)].append(word)

        return list(anagramMap.values())