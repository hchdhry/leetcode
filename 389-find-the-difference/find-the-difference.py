class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash = {}
        hashT = {}
        for char in s:
            hash[char] = hash.get(char,0)+1
        for char in t:
            hashT[char] = hashT.get(char,0)+1
        return list(filter(lambda X: hashT[X]-hash.get(X,0) >0,hashT))[0]
        