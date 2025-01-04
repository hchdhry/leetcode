from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(i):
            if i >= len(s):  
                res.append(partition.copy())
                return
            for j in range(i, len(s)):  
                if isPali(s, i, j): 
                    partition.append(s[i:j+1])  
                    backtrack(j + 1)  
                    partition.pop()  

        def isPali(string, l, r):
            while l < r:  
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True

        backtrack(0) 
        return res
