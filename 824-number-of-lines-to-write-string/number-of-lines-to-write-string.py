class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line = 1
        cur = 0
        for i in range(len(s)):
            w = widths[ord(s[i]) - ord('a')]  
            if cur + w > 100:  
                line += 1
                cur = 0  
            cur += w  
        return [line, cur]
