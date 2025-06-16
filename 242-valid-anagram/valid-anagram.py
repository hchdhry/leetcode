class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmapS = dict()
        hashmapT = dict()
        if len(s) != len(t):
            return False
        for char in s:
            hashmapS[char] = hashmapS.get(char,0) +1
        for char in t:
            hashmapT[char] = hashmapT.get(char,0) + 1
        for char in s:
            if hashmapT.get(char,0) != hashmapS.get(char,0):
                return False
        return True


        