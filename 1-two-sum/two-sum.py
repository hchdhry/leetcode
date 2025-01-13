class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, num in enumerate(nums):
            pair = target - num
            if pair in mydict:
                return [mydict[pair], i]
            mydict[num] = i