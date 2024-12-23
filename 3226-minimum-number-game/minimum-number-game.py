class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        output = []
        nums.sort(reverse = True)
        
        while nums:
            a = nums.pop()
            b = nums.pop()
            output.append(b)
            output.append(a)
        return output


                  


        
