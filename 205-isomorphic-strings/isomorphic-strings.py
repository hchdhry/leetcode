class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmapS = {}
        hashmapT = {}
        
        for i in range(len(s)):
            charS = s[i]
            charT = t[i]
            
            if charS in hashmapS:
                if hashmapS[charS] != charT:
                    return False
            else:
                hashmapS[charS] = charT
                
            if charT in hashmapT:
                if hashmapT[charT] != charS:
                    return False
            else:
                hashmapT[charT] = charS
        
        return True
