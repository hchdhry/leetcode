class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        hashmap = {}
        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        chars_to_match = len(hashmap)
        min_window = ""
        min_length = float('inf')
        
        while r < len(s):
            if s[r] in hashmap:
                hashmap[s[r]] -= 1
                if hashmap[s[r]] == 0:
                    chars_to_match -= 1
            
            while chars_to_match == 0:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_window = s[l:r+1]
                
                if s[l] in hashmap:
                    hashmap[s[l]] += 1
                    if hashmap[s[l]] > 0:
                        chars_to_match += 1
                l += 1
            
            r += 1
        
        return min_window