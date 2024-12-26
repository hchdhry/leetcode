class Solution:
    def countDigits(self, num: int) -> int:
        output = 0
        for number in str(num):
            if num % int(number) == 0:
                output+=1
        return output

        