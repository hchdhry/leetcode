class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        digitSum = 0
        for number in nums:
            elementSum += number
            for digit in str(number):
                digitSum += int(digit)
        return elementSum - digitSum
        