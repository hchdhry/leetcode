class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n

        res = self.fib(n-1) + self.fib(n-2)
        return res
        
        