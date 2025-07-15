class Solution:
    def isPalindrome(self, x: int) -> bool:
        string= str(x)
       
        return string[::-1] == str(x)
    