from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array
        closest_sum = float('inf')  # Initialize with a very large value
        
        for i in range(len(nums) - 2): 
            l, r = i + 1, len(nums) - 1  
            
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                
              
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                
         
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    return current_sum  
        return closest_sum
