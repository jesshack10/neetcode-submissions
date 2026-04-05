class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap = defaultdict(int)
        tmap = defaultdict(int)
        for c in s:
            smap[c] += 1
        
        for c in t:
            tmap[c] += 1

        return smap == tmap