class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        array1 = []
        array2 = []
        for word in word1:
            for char in word:
                array1.append(char)
        for word in word2:
            for char in word:
                array2.append(char)
        if len(array1) != len(array2):
            return False
        for i in range(len(array1)):
            if array1[i] != array2[i]:
                return False
        return True
        

        print(hash1.items())
        print(hash2.items())
        return hash1 == hash2
        
        