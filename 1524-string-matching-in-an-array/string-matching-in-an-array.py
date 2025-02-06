from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set() 
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] in words[j]: 
                    output.add(words[i]) 
        return list(output)  
