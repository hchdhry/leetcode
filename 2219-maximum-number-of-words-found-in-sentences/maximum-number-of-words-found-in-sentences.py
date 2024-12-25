class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = 0
        for sentence in sentences:
            spaces = 0
            for i in range(len(sentence)):
                if sentence[i] == " ":
                    spaces +=1
            output = max(output,spaces)
        return output+1    
            
                
