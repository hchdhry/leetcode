class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0
        length = len(s)
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for i in range(len(s) - 1):
            if hashmap[s[i]] < hashmap[s[i + 1]]:
                output -= hashmap[s[i]]
            else:
                output += hashmap[s[i]]
        output += hashmap[s[-1]]
        
        return output