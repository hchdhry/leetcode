class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap = {}
        for char in sentence:
            hashmap[char] =  hashmap.get(char,0)+1
        print(hashmap)
        return len(hashmap) == 26
        