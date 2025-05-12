class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        indexToChange = 0
        for i in nums:
            if i != val:
                nums[indexToChange] = i
                indexToChange += 1
        return indexToChange
 
      