class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      l,r = 0,0
      seen = set()
      max_length = 0
      while r<len(s):
         if s[r] not in seen:
            seen.add(s[r])
            max_length = max(max_length,r-l+1)
            r+=1
         else:
            seen.remove(s[l])
            l+=1
      return max_length  
         







