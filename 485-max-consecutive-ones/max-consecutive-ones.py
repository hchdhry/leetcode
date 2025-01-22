class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        output = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 1:
                output = max(cur,output)
                cur =0
            else:
                cur+=1
        output = max(cur, output)
        return output
