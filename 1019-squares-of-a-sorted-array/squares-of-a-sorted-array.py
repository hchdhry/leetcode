class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output = []
        for number in nums:
            output.append(number*number)
        output.sort()
        return output
        