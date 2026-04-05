class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        s1map = {}
        l,r = 0, len(s1) - 1
        window = {}

        #mapping s1
        for c in s1:
            s1map[c] = 1 + s1map.get(c, 0)

        #print(s1map)

        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)

            #print(window)

            #while windows size is invalid
            while (r - l + 1) > len(s1):
                window[s2[l]] = window[s2[l]] - 1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l += 1
            
            if window == s1map:
                return True

        return False

        