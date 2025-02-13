class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        char_sets = [set(word) for word in words]  
        lengths = [len(word) for word in words]
        curMax = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                if not (char_sets[i] & char_sets[j]):  
                    curMax = max(curMax, lengths[i] * lengths[j])

        return curMax
