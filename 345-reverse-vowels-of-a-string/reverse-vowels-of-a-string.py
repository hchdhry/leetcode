class Solution:
    def reverseVowels(self, s: str) -> str:
        stack = []
        output = ""
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        for char in s:
            if char in vowels:
                stack.append(char)
        print(stack)
        index = 0
        for char in s:
            if char in vowels:
                output+= stack.pop()
            else:
                output+=char
            index+=1
        return output

           
        
                

       

        