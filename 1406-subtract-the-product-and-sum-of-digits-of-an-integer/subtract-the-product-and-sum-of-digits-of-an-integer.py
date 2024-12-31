class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        products = 1
        for number in str(n):
            products*=int(number)
            sum  += int(number)
        return products - sum
        