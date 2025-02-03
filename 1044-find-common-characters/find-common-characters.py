class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])  
        
        for word in words[1:]:
            word_count = Counter(word)
            for char in common_count.keys():
                common_count[char] = min(common_count[char], word_count.get(char, 0))  
        
        result = []
        for char, freq in common_count.items():
            result.extend([char] * freq) 
        
        return result
