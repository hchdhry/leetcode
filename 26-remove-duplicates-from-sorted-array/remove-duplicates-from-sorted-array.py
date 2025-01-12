class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        index = 0
        for num in nums:
            if num not in seen:
                nums[index] = num
                seen.add(num)
                index+=1
        return index
       
