class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a new string containing only alphanumeric characters
        newstring = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the new string is equal to its reverse
        return newstring == newstring[::-1]