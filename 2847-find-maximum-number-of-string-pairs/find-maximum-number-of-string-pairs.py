class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        hash = {}
        for word in words:
            sorted_word = "".join(sorted(word))
            hash[sorted_word] = hash.get(sorted_word,0)+1
        return len(list(filter(lambda x: hash[x] == 2,hash)))


        
                
        