class Solution:
    def findMin(self, nums: List[int]) -> int:
        output = nums[0] 
        for i in range(len(nums)):
            if nums[i] < output:
                output = nums[i]
        
        return output