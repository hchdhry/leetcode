class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        shortest = min(strs, key=len)
        
        for i in range(len(shortest)):
            for string in strs:
                if string[i] != shortest[i]:
                    return shortest[:i]
        
        return shortest