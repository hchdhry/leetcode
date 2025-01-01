class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:  
            return s
        
        output = s[0]  
        n = len(s)
        
        for i in range(n):
          
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                cur = s[l:r+1]
                if len(cur) > len(output):
                    output = cur
                l -= 1
                r += 1
 
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                cur = s[l:r+1]
                if len(cur) > len(output):
                    output = cur
                l -= 1
                r += 1
        
        return output
