class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversedInput = str(x)
        return reversedInput == reversedInput[::-1]