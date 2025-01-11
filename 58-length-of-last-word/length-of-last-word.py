class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        lastLetter = -1
        lastSpace = -1
        
  
        for i in range(length-1, -1, -1):
            if s[i].isalpha():
                lastLetter = i
                break
       
        if lastLetter == -1:
            return 0
      
        for i in range(lastLetter, -1, -1):
            if s[i] == " ":
                lastSpace = i
                break
        
     
        return lastLetter - lastSpace
