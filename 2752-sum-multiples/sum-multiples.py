class Solution:
    def sumOfMultiples(self, n: int) -> int:
        Multiples = []
        for i in range(1,n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                Multiples.append(i)
        return sum(Multiples)
