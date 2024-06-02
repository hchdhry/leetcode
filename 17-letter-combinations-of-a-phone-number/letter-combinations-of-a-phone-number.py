class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        keys = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        combinations = []

        def backtrack(combination, index):
            if index == len(digits):
                combinations.append(combination)
                return

            for letter in keys[digits[index]]:
                backtrack(combination + letter, index + 1)

        backtrack('', 0)
        return combinations