class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = []
        length = len(nums)
        for number in nums:
            if number != 0:
                temp.append(number)
        for i in range(len(temp)):
            nums[i] = temp[i]
        for i in range(len(temp),len(nums)):
            nums[i] = 0

        