class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        positive = [] 
        negative = []
        for val in nums:
            if val < 0 :
                negative.append(val)
            else:
                positive.append(val)
        for i in range(len(positive)):
            if positive[i] and positive[i]*-1 in negative:
                return positive[i] 
        return -1
        
        