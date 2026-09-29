class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1map = [0] * 26
        window = [0] * 26

        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if s1map == window:
            return True

        for r in range(len(s1), len(s2)):

            letterIn = ord(s2[r]) - ord('a')
            window[letterIn] += 1

            letterOut = ord(s2[r - len(s1)]) - ord('a')
            window[letterOut] -= 1

            if s1map == window:
                return True

        return False

