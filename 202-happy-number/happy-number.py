class Solution:
    def isHappy(self, n: int) -> bool:
        def search(cur, seen):
            sum_of_squares = 0
            if cur == 1:
                return True
            if cur in seen:
                return False
            
            seen.add(cur)
            for num in str(cur):
                sum_of_squares += int(num) ** 2
             
            return search(sum_of_squares, seen)
        
        return search(n, set())
