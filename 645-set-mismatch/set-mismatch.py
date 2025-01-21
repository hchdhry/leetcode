class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        map = {}
        duplicate = 0
        missing = 0
        
     
        for num in nums:
            map[num] = map.get(num, 0) + 1
       
        for i in range(1, len(nums) + 1):
            if map.get(i, 0) == 2:
                duplicate = i
            elif map.get(i, 0) == 0:
                missing = i
        
        return [duplicate, missing]