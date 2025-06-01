class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
       
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  

     
        a = abs(dividend)
        b = abs(divisor)
        result = 0

      
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            result += multiple

       
        if (dividend < 0) ^ (divisor < 0):
            result = -result

        return result
