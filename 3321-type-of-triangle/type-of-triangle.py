class Solution:
    def triangleType(self, nums: List[int]) -> str:
        hashmap = {}
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        for side in nums:
            hashmap[side] = hashmap.get(side,0)+1
        

        match max(hashmap.values()):
            case 1:
                return "scalene"
            case 2:
                return "isosceles"
            case 3:
                return "equilateral" 
   
        
        

            


        
            

        
        