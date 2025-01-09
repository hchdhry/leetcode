class Solution:
    def isHappy(self, n: int) -> bool:
        def search(cur, seen):
            if cur == 1:
                return True
            if cur in seen:
                return False
            
            seen.add(cur)
            sum_of_squares = sum(int(num) ** 2 for num in str(cur))
            return search(sum_of_squares, seen)
        
        return search(n, set())
