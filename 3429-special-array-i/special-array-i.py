class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l,r = 0,1
        n = len(nums)
        if n<2:
            return True
        while r<n:
            if nums[l]%2 == nums[r]%2:
                return False
            print(l,r)
            l+=1
            r+=1
        return True
        
        
        