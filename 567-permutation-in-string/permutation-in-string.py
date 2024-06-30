class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        n = len(s1)
        s1_sorted = sorted(s1)

        for i in range(len(s2) - n + 1):
            window = s2[i:i+n]
            if sorted(window) == s1_sorted:
                return True

        return False