class Solution:
    def minElement(self, nums: List[int]) -> int:
        output = None
        for num in nums:
            cur = 0
            for char in str(num):
                cur += int(char)
            

            
            if output == None:
                output = cur
            output = min(output,cur)
        return output

        