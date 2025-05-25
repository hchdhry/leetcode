class Solution:
    def mySqrt(self, x: int) -> int:
        found = False
        cur = 0
        while not found:
            if cur * cur > x:
                return cur -1
                found = True
            cur +=1

        
        