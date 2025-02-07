class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        hash = {}
        output = None
        for char in licensePlate:
            if char.isalpha():
                char = char.lower()
                hash[char] = hash.get(char,0)+1
        for word in words:
            copy = hash.copy()
            for char in word:
                char = char.lower()
                if char in copy and copy[char]>0:
                    copy[char] = copy.get(char)-1

            if sum(copy.values()) == 0:
                if output is None or len(word) < len(output):  
                    output = word  
           
        return output

