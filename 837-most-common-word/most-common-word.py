class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    
        cleaned_paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        
        word_count = {}
        banned_set = set(word.lower() for word in banned) 
        words = cleaned_paragraph.split()  

        for word in words:
            if word not in banned_set:
                word_count[word] = word_count.get(word, 0) + 1

        return max(word_count, key=word_count.get)
