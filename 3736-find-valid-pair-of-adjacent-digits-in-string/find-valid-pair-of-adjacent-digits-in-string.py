class Solution:
    def findValidPair(self, string: str) -> str:
        count = Counter(string)

        for a, b in pairwise(string):
            if a != b and count[a] == int(a) and count[b] == int(b):
                return a + b

        return ''