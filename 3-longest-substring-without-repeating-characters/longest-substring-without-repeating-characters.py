class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0 
        seen = set()
        output = 0
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])  
                output = max(output,r-l+1) 
                r+=1
            else:
                seen.remove(s[l])
              
                l+=1
        return output



         







