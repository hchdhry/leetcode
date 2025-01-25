class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       
        n = len(nums)+1
        for i in range(n):
            if i not in nums :
                return i
            
    

        