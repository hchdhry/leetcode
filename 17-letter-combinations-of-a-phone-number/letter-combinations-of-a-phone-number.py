class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keys = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        def backtrack(i,cur):
            if len(cur) == len(digits):
                res.append(cur)
                return
            currentLetter = digits[i]
            for letter in keys[currentLetter]:
                cur += letter
                backtrack(i+1,cur)
                cur = cur[:-1]
        backtrack(0,"")
        return res
            
