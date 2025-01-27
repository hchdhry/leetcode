class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
       
        for word in words:
            lower_word = word.lower()
            if lower_word[0] in row1:
                cur = row1
            elif lower_word[0] in row2:
                cur = row2
            else:
                cur = row3
            if all(char in cur for char in lower_word):
                output.append(word)
        return output
                 
               



        